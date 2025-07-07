from bottle import request, redirect, response, route
from services.user_service import user_service
from bottle import template

def require_login():
    user = request.get_cookie("logged_user")
    if not user:
        return redirect('/login')


@route('/login', method='POST')
def login():
    email = request.forms.get('email')
    senha = request.forms.get('senha')  # senha vinda do form

    for user in user_service.get_all_users():
        if user.email == email and user.senha == senha:
            response.set_cookie('logged_user', user.name, path='/')
            response.set_cookie('usuario_id', str(user.id), path='/')
            redirect('/usuarios')

    return template('login.tpl', erro="Credenciais inválidas")



@route('/logout')
def logout():
    response.delete_cookie("logged_user", path='/')
    response.delete_cookie("usuario_id", path='/')
    redirect('/login')
