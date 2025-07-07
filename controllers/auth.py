from bottle import request, redirect, route, response, template
import bcrypt
from services.user_service import user_service


def require_login():
    """Middleware para proteger rotas: redireciona para login se não autenticado."""
    if not request.get_cookie("user"):
        redirect('/login')

@route('/login', method='POST')
def login():
    email = request.forms.get('email')
    senha = request.forms.get('senha')

    for user in user_service.get_all_users():
        if user.email == email and bcrypt.checkpw(senha.encode('utf-8'), user.senha_hash):
            response.set_cookie('logged_user', user.name, path='/')
            response.set_cookie('usuario_id', str(user.id), path='/')
            return redirect('/usuarios')

    return template('login.tpl', erro="Credenciais inválidas")
