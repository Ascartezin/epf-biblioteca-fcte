from bottle import request, redirect, response, route, template
from services.user_service import user_service

SECRET_KEY = 'Batata-Frita-Eh-Bom-Mas-Mude-Essa-Senha-123!'

def require_login(func):
    def wrapper(*args, **kwargs):
        user_cookie = request.get_cookie("logged_user", secret=SECRET_KEY)
        if user_cookie:
            return func(*args, **kwargs)
        else:
            return redirect('/login')
    return wrapper

@route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        user = user_service.find_user_by_email(email)
        if user and user.verificar_senha(senha):
            response.set_cookie('logged_user', user.email, secret=SECRET_KEY, path='/')
            return redirect('/usuarios')
        return template('login.tpl', erro="Email ou senha inválidos.", title='Login')
    return template('login.tpl', erro=None, title='Login')

@route('/logout')
def logout():
    response.delete_cookie("logged_user", path='/')
    redirect('/login')

@route('/')
def index():
    redirect('/login')