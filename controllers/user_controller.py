from bottle import route, template, request, redirect
from services.user_service import UserService
from models.user import User
<<<<<<< HEAD
from controllers.auth_controller import require_login
from bottle import response
from models import User
=======
from controllers.auth import require_login
from bottle import response, redirect
>>>>>>> a0ec61135a51c803a83e64b0493626b88adc2a15


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
    senha = request.forms.get('senha')  

    user = User(id=id, name=name, email=email, birthdate=birthdate, senha=senha)
    user_service.add_user(user)
    redirect('/usuarios')



@route('/usuarios/editar/<user_id:int>')
def editar_usuario_form(user_id):
    require_login()
    user = user_service.find_user_by_id(user_id)
    if user:
        return template('user_form.tpl', usuario=user, title='Editar Usuário')
    return "Usuário não encontrado"


@route('/usuarios/atualizar', method='POST')
def atualizar_usuario():
    require_login()

    id = int(request.forms.get('id'))
    name = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')
    senha = request.forms.get('senha')

    user_existente = user_service.find_user_by_id(id)
    if not user_existente:
        return "Usuário não encontrado"

    if senha:
        user_service.update_user(id, name=name, email=email, birthdate=birthdate, senha=senha)
    else:
        user_service.update_user(id, name=name, email=email, birthdate=birthdate)

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
<<<<<<< HEAD
            response.set_cookie("usuario_id", str(user.id), path='/')  # ✅ NOVO COOKIE
            redirect('/emprestimos')  # ou outra rota inicial
    return template('login.tpl', erro="Credenciais inválidas")
=======
            response.set_cookie("usuario_id", str(user.id), path='/')  # ✅ novo cookie com o ID
            redirect('/usuarios')
    
    return template('login.tpl', erro="Credenciais inválidas", title='Login')
>>>>>>> a0ec61135a51c803a83e64b0493626b88adc2a15

def require_login():
    if not request.get_cookie("usuario_id"):
        redirect('/login')

<<<<<<< HEAD
@route('/usuarios/editar/<user_id:int>')
def editar_usuario_form(user_id):
    require_login()
    user = user_service.find_user_by_id(user_id)
    if user is None:
        return template('erro.tpl', mensagem="Usuário não encontrado.")
    return template('user_form.tpl', usuario=user)
=======
@route('/logout')
def logout():
    response.delete_cookie('usuario_id')
    redirect('/')
>>>>>>> a0ec61135a51c803a83e64b0493626b88adc2a15
