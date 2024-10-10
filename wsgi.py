import sys
from dotenv import dotenv_values
from pathlib import Path
from datetime import timedelta
from cachelib.file import FileSystemCache

# Establece la configuración de la aplicación
class Config:
    # Indica si se está en modo depuración o no
    DEBUG = True
    # Calcula el directorio raiz de la aplicación
    DOCUMENT_ROOT = Path(__file__).parent.as_posix()
    # Lee las variables de entorno a un diccionario
    ENV_VARS = dotenv_values(f'{DOCUMENT_ROOT}/.env')
    # Necesario para las sesiones
    SECRET_KEY=ENV_VARS['SECRET_KEY']
    # Sesión basada en archivos temporales del servidor
    SESSION_TYPE='cachelib'
    # Utilizando un límite de sesiones antes de hacer limpieza y estableciendo
    # el directorio donde las mismas se almacenarán
    SESSION_CACHELIB=FileSystemCache(threshold=500,
        cache_dir=f'{DOCUMENT_ROOT}/flask_sessions')
    # Si se hace la sesión permanente, el tiempo que durará
    PERMANENT_SESSION_LIFETIME=timedelta(days=5)
    # Sistema gestor de BBDD utilizado
    SQLALCHEMY_DATABASE_URI=f'mysql+mysqlconnector://{
        ENV_VARS['DB_USERNAME']}:{ENV_VARS['DB_PASSWORD']
        }@localhost:3306/blog_posts'
    # SQLALCHEMY_DATABASE_URI='sqlite:///blog_posts.db'
    # Tamañno máximo del upload al servidor
    MAX_CONTENT_LENGTH=4 * 1024 * 1024
    
    # Configuraciones específicas de la aplicación
    # Longitud máxima del nombre del fichero de imagen de perfil
    PROFILE_IMG_FILENAME_MAX_LEN=128
    # Máxima longitud de la URL de un post
    POST_URL_MAX_LEN=128
    # Máxima longitud del título de un post
    POST_TITLE_MAX_LEN=128
    # Máxima longitud de la descripción de un post
    POST_DESC_MAX_LEN=256
    # Máxima longitud del contenido de un post
    POST_CONTENT_MAX_LEN=16384

# Importa de la ruta correcta para acceder a la aplicación
sys.path.insert(0, Config.DOCUMENT_ROOT)
from blogposts import create_app

# Crea la aplicación
application = create_app(Config)

if __name__ == '__main__':
    application.run()	
