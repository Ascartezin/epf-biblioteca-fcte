from bottle import route, template, request, redirect, response
from services.user_service import UserService
from models.user import User
from controllers.auth import require_login
import bcrypt
import bottle

# Torna o objeto request acessível em todos os templates
bottle.BaseTemplate.defaults['request'] = request

# Instancia o serviço de usuários
user_service = UserService()


# Lista todos os usuários
@route('/usuarios')
def listar_usuarios():
    require_login()
    users = user_service.get_all_users()
    return template('users.tpl', usuarios=users, title='Usuários')


# Formulário para novo usuário
@route('/usuarios/novo')
def novo_usuario_form():
    require_login()
    return template('user_form.tpl', usuario=None, erro=None, title='Novo Usuário')


# Criação de novo usuário
@route('/usuarios/criar', method='POST')
def criar_usuario():
    require_login()

    name = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')
    senha = request.forms.get('senha')

    erro = validar_usuario(name, email, birthdate, senha)
    if erro:
        usuario_dict = {'name': name, 'email': email, 'birthdate': birthdate}
        return template('user_form.tpl', usuario=usuario_dict, erro=erro, title='Novo Usuário')

    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    user = User(id=None, name=name, email=email, birthdate=birthdate, senha_hash=senha_hash)
    user_service.add_user(user)
    redirect('/usuarios')


# Formulário de edição
@route('/usuarios/editar/<user_id:int>')
def editar_usuario_form(user_id):
    require_login()
    user = user_service.find_user_by_id(user_id)
    if user:
        return template('user_form.tpl', usuario=user, erro=None, title='Editar Usuário')
    return "Usuário não encontrado"


# Atualização de dados do usuário
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

    erro = validar_usuario(name, email, birthdate, senha if senha else None)
    if erro:
        # Atualiza os dados para mostrar no form
        user_existente.name = name
        user_existente.email = email
        user_existente.birthdate = birthdate
        return template('user_form.tpl', usuario=user_existente, erro=erro, title='Editar Usuário')

    if senha:
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        user_service.update_user(id, name=name, email=email, birthdate=birthdate, senha_hash=senha_hash)
    else:
        user_service.update_user(id, name=name, email=email, birthdate=birthdate)

    redirect('/usuarios')


# Deletar usuário
@route('/usuarios/deletar/<user_id:int>')
def deletar_usuario(user_id):
    require_login()
    user_service.delete_user(user_id)
    redirect('/usuarios')


# Validação de dados do usuário
def validar_usuario(name, email, birthdate, senha=None):
    import re
    if not name or not email or not birthdate:
        return "Nome, email e data de nascimento são obrigatórios."

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Email inválido."

    try:
        from datetime import datetime
        datetime.strptime(birthdate, '%Y-%m-%d')
    except ValueError:
        return "Data de nascimento inválida."

    if senha is not None and len(senha) < 6:
        return "Senha deve ter ao menos 6 caracteres."

    return None
