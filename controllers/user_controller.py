from bottle import route, template, request, redirect
from services.user_service import UserService
from models.user import User
from controllers.auth import require_login
from bottle import response, redirect


user_service = UserService()

@route('/usuarios')
def listar_usuarios():
    users = user_service.get_all_users()
    return template('users.tpl', usuarios=users, title='Usuários')

@route('/usuarios/novo')
def novo_usuario_form():
    require_login()
    return template('user_form.tpl', usuario=None, title='Novo Usuário')



@route('/usuarios/criar', method='POST')
def criar_usuario():
    require_login()
    id = int(request.forms.get('id'))  
    name = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')

    user = User(id=id, name=name, email=email, birthdate=birthdate)
    user_service.add_user(user)
    redirect('/usuarios')


@route('/usuarios/editar/<user_id:int>')
def editar_usuario_form(user_id):
    require_login()
    user = user_service.find_user_by_id(user_id)
    if user:
        return template('user_form.tpl', usuario=user, title='Editar Usuário')
    return "Usuário não encontrado"


@route('/usuarios/atualizar/<user_id:int>', method='POST')
def atualizar_usuario(user_id):
    require_login()
    name = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')

    user_service.update_user(user_id, name=name, email=email, birthdate=birthdate)
    redirect('/usuarios')


@route('/usuarios/deletar/<user_id:int>')
def deletar_usuario(user_id):
    require_login()
    user_service.delete_user(user_id)
    redirect('/usuarios')

#
@route('/login', method='GET')
def login_form():
    return template('login.tpl', title='Login')


@route('/login', method='POST')
def login():
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')

    for user in user_service.get_all_users():
        if user.email == email and user.birthdate == birthdate:
            response.set_cookie("logged_user", user.name, path='/')
            response.set_cookie("usuario_id", str(user.id), path='/')  # ✅ novo cookie com o ID
            redirect('/usuarios')
    
    return template('login.tpl', erro="Credenciais inválidas", title='Login')

def require_login():
    if not request.get_cookie("usuario_id"):
        redirect('/login')

@route('/logout')
def logout():
    response.delete_cookie('usuario_id')
    redirect('/')
