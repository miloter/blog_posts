from flask import Blueprint, render_template, request
from blogposts.models.user import User
from blogposts.models.post import Post

bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        posts = search_posts(request.form['search'])
        value = 'hidden'
    else:
        posts = Post.query.all()
        value = ''
    return render_template('home/index.html', posts = posts,
        get_user=get_user, value=value)

@bp.route('/blog/<url>')
def blog(url):
    post = Post.query.filter_by(url=url).first()
    return render_template('home/blog.html', post=post, get_user=get_user)

def get_user(id):
    '''Devuelve un usuario a partir de su ID'''
    return User.query.get(id)

def search_posts(query):
    posts = Post.query.filter(Post.title.ilike(f'%{query}%')).all()    
    return posts