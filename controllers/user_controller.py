from bottle import route, template, request, redirect
from services.user_service import UserService
from models.user import User
from controllers.auth_controller import require_login
from bottle import response
from models import User


user_service = UserService()

@route('/usuarios')
def listar_usuarios():
    users = user_service.get_all_users()
    return template('users.tpl', usuarios=users)

@route('/usuarios/novo')
def novo_usuario_form():
    require_login()
    return template('user_form.tpl', usuario=None)



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
        return template('user_form.tpl', usuario=user)
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
@route('/login')
def login_form():
    return template('login.tpl')


@route('/login', method='POST')
def login():
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')

    for user in user_service.get_all_users():
        if user.email == email and user.birthdate == birthdate:
            response.set_cookie("logged_user", user.name, path='/')
            response.set_cookie("usuario_id", str(user.id), path='/')  # ✅ NOVO COOKIE
            redirect('/emprestimos')  # ou outra rota inicial
    return template('login.tpl', erro="Credenciais inválidas")

def require_login():
    if not request.get_cookie("usuario_id"):
        redirect('/login')

@route('/usuarios/editar/<user_id:int>')
def editar_usuario_form(user_id):
    require_login()
    user = user_service.find_user_by_id(user_id)
    if user is None:
        return template('erro.tpl', mensagem="Usuário não encontrado.")
    return template('user_form.tpl', usuario=user)
