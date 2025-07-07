from bottle import route, template, request, redirect, abort
from controllers.auth import require_login
from services.livro_service import livro_service
from models.livro import Livro

@route('/livros')
@require_login
def listar_livros():
    todos_os_livros = livro_service.get_all_livros()
    return template('livros_list.tpl', 
                    livros=todos_os_livros, 
                    title="Acervo de Livros")

@route('/livros/novo')
@require_login
def novo_livro_form():
    return template('livro_form.tpl', livro=None, erro=None, title='Adicionar Novo Livro')

@route('/livros/criar', method='POST')
@require_login
def criar_livro():
    titulo = request.forms.get('titulo')
    autor = request.forms.get('autor')

    if not titulo or not autor:
        erro = "Título e autor são obrigatórios."
        return template('livro_form.tpl', livro=None, erro=erro, title='Adicionar Novo Livro')
    
    novo_livro = Livro(id=None, titulo=titulo, autor=autor)
    livro_service.add_livro(novo_livro)
    redirect('/livros')

@route('/livros/editar/<livro_id:int>')
@require_login
def editar_livro_form(livro_id):
    livro = livro_service.find_livro_by_id(livro_id)
    if not livro:
        return abort(404, "Livro não encontrado.")
    return template('livro_form.tpl', livro=livro, erro=None, title='Editar Livro')

@route('/livros/atualizar', method='POST')
@require_login
def atualizar_livro():
    livro_id = int(request.forms.get('id'))
    titulo = request.forms.get('titulo')
    autor = request.forms.get('autor')

    if not titulo or not autor:
        livro = livro_service.find_livro_by_id(livro_id)
        erro = "Título e autor são obrigatórios."
        return template('livro_form.tpl', livro=livro, erro=erro, title='Editar Livro')
    
    livro_service.update_livro(livro_id, titulo=titulo, autor=autor)
    redirect('/livros')

@route('/livros/deletar/<livro_id:int>', method='POST')
@require_login
def deletar_livro(livro_id):
    livro_service.delete_livro(livro_id)
    redirect('/livros')