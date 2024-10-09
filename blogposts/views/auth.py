from flask import (
    Blueprint, render_template, request, url_for,
     redirect, flash, session, g, current_app
)
from werkzeug.security import generate_password_hash, check_password_hash
from blogposts import db
from blogposts.models.user import User
from blogposts.utils.login_manager import login_on, login_required
from blogposts.utils.httpparams import Util, Param, Filename

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
@login_on
def register():
    if request.method == 'POST':
        param = Param()
        email = param.validate(request.form['email'], Util.RE_EMAIL,
            Util.ERR_EMAIL, max_length=32, field_title='e-mail')
        username = param.validate(request.form['username'], Util.RE_USERNAME,
            Util.ERR_USERNAME, max_length=16, field_title='Usuario')        
        password = param.validate(request.form['password'], Util.RE_PASSWORD,
            Util.ERR_PASSWORD, max_length=32, field_title='Contraseña')
        
        # Comprobamos la existencia del usuario        
        if User.query.filter_by(username=username).first():
            param.add_error(f'Ya existe un usario "{username}"')
        if param.is_error():
            for msg in param.get_msgs():
                flash(msg['message'], msg['category'])
            # Para pasarlo en la plantilla
            user = User(username, email, password)
        else:            
            # Nuevo usuario
            user = User(username, email, generate_password_hash(password))
            db.session.add(user)
            db.session.commit()            
            flash('Usuario registrado con éxito', 'info')
            return redirect(url_for('auth.login'))        
    else:
        user = None
    return render_template('auth/register.html', user=user)

@bp.route('/login', methods=['GET', 'POST'])
@login_on
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        # Comprobamos la existencia del usuario
        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password, password):
            flash('Usuario o contraseña incorrectos', 'error')           
        else:
            # Se inicia sesión y se redirige a la lista de posts
            session['user_id'] = user.id            
            return redirect(url_for('post.posts'))            
    else:
        username = ''
        password = ''
    return render_template('auth/login.html', username=username, password=password)

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():    
    if request.method == 'POST':
        param = Param()
        check_filename = Filename()
        email = param.validate(request.form['email'], Util.RE_EMAIL,
            Util.ERR_EMAIL, max_length=32, field_title='e-mail')
        username = param.validate(request.form['username'], Util.RE_USERNAME,
            Util.ERR_USERNAME, max_length=16, field_title='Usuario')
        password = param.validate(request.form['password'], Util.RE_PASSWORD,
            Util.ERR_PASSWORD, ignore_empty=True,
            max_length=32, field_title='Contraseña')        
        file_photo = request.files['photo']     
        filename = check_filename.validate(filename=file_photo.filename,
            max_length=current_app.config.get('PROFILE_IMG_FILENAME_MAX_LEN'),
            re_ext=Util.RE_IMG_EXT, field_title='Seleccionar archivo')

        # Si el nombre de usuario cambió, comprobamos que no exista        
        if g.user.username != username:
            if User.query.filter_by(username=username).first():
                param.add_error(f'Ya existe un usario "{username}"')        
        is_error = param.is_error() or check_filename.is_error()
        if is_error:            
            # Para pasarlo en la plantilla
            user = User(username, email, password, g.user.photo)
        if param.is_error():
            for msg in param.get_msgs():
                flash(msg['message'], msg['category'])            
        if check_filename.is_error():           
            for msg in check_filename.get_msgs():
                flash(msg['message'], msg['category'])
        if not is_error:
            # Actualiza el usuario
            user = User.query.get(g.user.id)
            # Si hay foto, se intenta guardar            
            if filename:
                path = f'media/{filename}'                
                file_photo.save(f'{current_app.static_folder}/{path}')
                # Guardamos en el registro la ruta relativa de la foto            
                user.photo = path
            user.email = email
            user.username = username
            if password:
                user.password = generate_password_hash(password)
            db.session.commit()
            # Actualiza los datos de sesión
            g.user = user
            flash('Perfil actualizado con éxito', 'info')                    
    else:
        user = g.user
    return render_template('auth/profile.html', user=user)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.index'))

@bp.before_app_request
def load_session_data():    
    '''Función decorada con @bp.before_app_request para que recupere
    el usuario autenticado en la sesión en el objeto g.user, o bien
    g.user será None si no hay ningún usuario autenticado.'''    
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
