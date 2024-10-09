import functools
from flask import redirect, url_for, g

def login_required(view):
    '''Función decoradora: Comprueba si una view requiere auntenticación:
    Si el usuario ha iniciado sesión se podrá cargar la view y en caso
    contrario, se le redirigirá a la página de login.'''
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(*args, **kwargs)
    return wrapped_view

def login_on(view):
    '''Función decoradora: Si una view se usa cuando no hay una sesión iniciada
    se llamará a esta view pasándole. Si el usuario ha iniciado sesión se le
     redigirá a la página predeterminada, en otro caso se podrá cargar la view.'''
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return view(*args, **kwargs)
        return redirect(url_for('post.posts'))
    return wrapped_view
