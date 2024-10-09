from datetime import datetime
# Para poder manejar en MySQL un DateTime con microsegundos
from sqlalchemy.dialects.mysql import DATETIME
from blogposts import db

class Post(db.Model):
    # Nombres de tabla en plural
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    url = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.Text)
    content = db.Column(db.Text)
    # En SQLite o si no se quieren fracciones de segundo
    # created = db.Column(db.DateTime(), default=datetime.now())
    created = db.Column(DATETIME(fsp=6), default=datetime.now())

    def __init__(self, user_id, url, title, desc, content) -> None:        
        self.user_id = user_id
        self.url = url
        self.title = title
        self.desc = desc
        self.content = content

    def __repr__(self) -> str:
        return f'<Post: {self.title}>'