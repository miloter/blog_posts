from blogposts import db

class User(db.Model):
    # Nombres de tabla en plural
    __tablename__ = 'users'
    # Campos estáticos que definen la tabla
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(32), nullable=False)
    password = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(128))

    def __init__(self, username, email, password, photho = None) -> None:        
        self.username = username
        self.email = email
        self.password = password
        self.photo = photho

    def __repr__(self) -> str:
        return f'<User: {self.username}>'