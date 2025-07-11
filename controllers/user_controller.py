from bottle import route, template, request, redirect, abort
from services.user_service import user_service
from models.user import User
from controllers.auth import require_login
import bcrypt
import re
from datetime import datetime

@route('/usuarios/novo')
def novo_usuario_form():
    return template('user_form.tpl', usuario=None, erro=None, title='Criar Nova Conta')

@route('/usuarios/criar', method='POST')
def criar_usuario():
    name = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')
    senha = request.forms.get('senha')

    erro = validar_usuario(name, email, birthdate, senha)
    if erro:
        usuario_temporario = User.from_dict({'name': name, 'email': email, 'birthdate': birthdate})
        return template('user_form.tpl', usuario=usuario_temporario, erro=erro, title='Criar Nova Conta')
    
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    user = User(id=None, name=name, email=email, birthdate=birthdate, senha_hash=senha_hash)
    
    if user_service.add_user(user):
        redirect('/login')
    else:
        erro = f"O email '{email}' já está em uso."
        usuario_temporario = User.from_dict({'name': name, 'email': email, 'birthdate': birthdate})
        return template('user_form.tpl', usuario=usuario_temporario, erro=erro, title='Criar Nova Conta')

@route('/usuarios')
@require_login
def listar_usuarios():
    users = user_service.get_all_users()
    return template('users.tpl', usuarios=users, title='Gerenciar Usuários')

@route('/usuarios/editar/<user_id:int>')
@require_login
def editar_usuario_form(user_id):
    user = user_service.find_user_by_id(user_id)
    if not user:
        return abort(404, "Usuário não encontrado.")
    return template('user_form.tpl', usuario=user, erro=None, title='Editar Usuário')

@route('/usuarios/atualizar', method='POST')
@require_login
def atualizar_usuario():
    user_id = int(request.forms.get('id'))
    name = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')
    senha = request.forms.get('senha')

    user_existente = user_service.find_user_by_id(user_id)
    if not user_existente:
        abort(404, "Usuário não encontrado.")

    erro = validar_usuario(name, email, birthdate, senha if senha else None)
    if erro:
        dados_submetidos = User.from_dict({'id': user_id, 'name': name, 'email': email, 'birthdate': birthdate})
        return template('user_form.tpl', usuario=dados_submetidos, erro=erro, title='Editar Usuário')

    dados_atualizacao = {'name': name, 'email': email, 'birthdate': birthdate}
    if senha:
        dados_atualizacao['senha_hash'] = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    user_service.update_user(user_id, **dados_atualizacao)
    redirect('/usuarios')

@route('/usuarios/deletar/<user_id:int>', method='POST')
@require_login
def deletar_usuario(user_id):
    if not user_service.find_user_by_id(user_id):
        abort(404, "Usuário não encontrado para deletar.")
    user_service.delete_user(user_id)
    redirect('/usuarios')

def validar_usuario(name, email, birthdate, senha=None):
    if not name or not email or not birthdate:
        return "Nome, email e data de nascimento são obrigatórios."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Email inválido."
    try:
        datetime.strptime(birthdate, '%Y-%m-%d')
    except ValueError:
        return "Data de nascimento inválida. Use o formato AAAA-MM-DD."
    if senha and len(senha) < 6:
        return "Senha deve ter ao menos 6 caracteres."
    return None