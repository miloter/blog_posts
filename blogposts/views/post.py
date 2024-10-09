import re
from flask import (
    Blueprint, render_template, request, url_for, redirect,
    flash, session, g, current_app
)
from blogposts import db
from blogposts.models.post import Post
from blogposts.utils.login_manager import login_required
from blogposts.utils.httpparams import Util, Param
from blogposts.utils.similwords import SimilWords

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/posts')
@login_required
def posts():
    posts = Post.query.all()        
    return render_template('post/posts.html', posts=posts)

@bp.route('/create', methods=['GET', 'POST'])    
@login_required
def create():
    if request.method == 'POST':
        param = Param()        
        cfg = current_app.config.get
        title = param.validate(request.form['title'], re=Util.RE_ANY_WORD_CHAR,
            msg_error='''El título tendrá al menos una letra, dígito,
            guión bajo o guión medio''', max_length=cfg('POST_TITLE_MAX_LEN'),
            field_title='Título')
        if not param.is_error() and Post.query.filter_by(title=title).first():
            param.add_error(f'El título "{title}" ya existe en otro post')
        desc = param.validate(request.form['desc'], Util.RE_STR,        
            msg_error='Descripción no admitida',
            max_length=cfg('POST_DESC_MAX_LEN'), ignore_empty=True,
            field_title='Descripción')
        content = param.validate(request.form['content'],
            Util.RE_STR, msg_error='Contenido no admitido',
            max_length=cfg('POST_CONTENT_MAX_LEN'), ignore_empty=True,
            field_title='Contenido')
        post = Post(g.user.id, SimilWords(to_lower=True).normalize(
            title, delimiter='-'), title, desc, content)
        if param.is_error():
            for msg in param.get_msgs():
                flash(msg['message'], msg['category'])
        else:
            db.session.add(post)
            db.session.commit()            
            flash(f'Entrada con título "{title}" creada con éxito', 'success')
    else:
        post = None
    return render_template('post/create.html', post=post)

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    post = Post.query.get(id)
    # Hay que comprobar que haya un post con ese id    
    if not post:
        flash(f'No existe ningún post el id {id}', 'warning')
        return redirect(url_for('post.posts'))
    if request.method == 'POST':
        param = Param()                
        cfg = current_app.config.get
        title = param.validate(request.form['title'], re=Util.RE_ANY_WORD_CHAR,
            msg_error='''El título tendrá al menos una letra, dígito,
            guión bajo o guión medio''', max_length=cfg('POST_TITLE_MAX_LEN'),
            field_title='Título')        
        # Hay que comprobar que el título no exista en otro post
        post_by_title = Post.query.filter_by(title=title).first()
        if not param.is_error() and post_by_title and id != post_by_title.id:            
            param.add_error(f'El título "{title}" ya existe en otro post')        
        desc = param.validate(request.form['desc'], Util.RE_STR,        
            msg_error='Descripción no admitida',
            max_length=cfg('POST_DESC_MAX_LEN'), ignore_empty=True,
            field_title='Descripción')
        content = param.validate(request.form['content'],
            Util.RE_STR, msg_error='Contenido no admitido',
            max_length=cfg('POST_CONTENT_MAX_LEN'), ignore_empty=True,
            field_title='Contenido')                
        if param.is_error():
            for msg in param.get_msgs():
                flash(msg['message'], msg['category'])
        else:
            post.url = SimilWords(to_lower=True).normalize(title, delimiter='-')
            post.title = title
            post.desc = desc
            post.content = content
            db.session.commit()            
            flash(f'Post actualizado con éxito', 'success')
    return render_template('post/update.html', post=post)

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get(id)
    # Hay que comprobar que haya un post con ese id    
    if post:
        db.session.delete(post)
        db.session.commit()
        flash('Post eliminado con éxito', 'success')
    else:
        flash(f'No existe ningún post el id {id}', 'warning')        
    return redirect(url_for('post.posts'))
