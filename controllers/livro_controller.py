from bottle import route, template, request, redirect
import services.livro_service as livro_service
from models.livro import Livro

@route('/livros')
def listar_livros():
    livros = livro_service.get_all()
    return template('livros', livros=livros)

@route('/livros/novo')
def novo_livro():
    return template('livro_form', livro=None)

@route('/livros', method='POST')
def criar_livro():
    titulo = request.forms.get('titulo')
    autor = request.forms.get('autor')
    id = str(hash(titulo + autor))[:8]  # Gera um ID simples
    livro = Livro(id=id, titulo=titulo, autor=autor)
    livro_service.add_livro(livro)
    redirect('/livros')

@route('/livros/<id>/edit')
def editar_livro(id):
    livro = livro_service.get_by_id(id)
    return template('livro_form', livro=livro)

@route('/livros/<id>', method='POST')
def atualizar_livro(id):
    titulo = request.forms.get('titulo')
    autor = request.forms.get('autor')
    livro_service.update_livro(id, {
        'titulo': titulo,
        'autor': autor
    })
    redirect('/livros')

@route('/livros/<id>/delete')
def deletar_livro(id):
    livro_service.delete_livro(id)
    redirect('/livros')
