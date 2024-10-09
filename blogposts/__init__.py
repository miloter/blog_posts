from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

# Para que otros módulos puedan referenciar la base de datos
db = SQLAlchemy()

def create_app(config) -> Flask:
    # Representa a la aplicación Flask
    app = Flask(__name__)    
    
    # Cargamos la configuración de la aplicación    
    app.config.from_object(config)

    # Inicia el ORM de la aplicación
    db.init_app(app)

    # Establece la sesión basada en almacenamiento de sesiones en el servidor
    Session(app)

    # Para la gestión de los ficheros propios de la aplicación
    app.static_folder = f'{app.config['DOCUMENT_ROOT']}/blogposts/static'        

    # Registra las vistas en este punto, que 'db' ya está definida
    from blogposts.views import home, auth, post
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(post.bp)
    
    # Migramos los modelos a la BBDD
    with app.app_context():        
        db.create_all()

    # Se puede poner un filtro personalizado en las plantilass Jinja
    # de Flask para formatear valores:
    @app.add_template_filter
    def flash_category_to_alert_class(category):
        '''Plantilla flask personalizada para covertir categorías de
        mensajes flash, a clases bootstrap'''
        return {
            'info': 'alert-info',
            'success': 'alert-success',
            'warning': 'alert-warning',
            'error': 'alert-danger',
            'message': 'alert-info'
        }.get(category, 'alert-info')
            
    
    return app