from bottle import route, request, template, redirect
from controllers.auth_controller import require_login
from services.emprestimo import EmprestimoService
from services.user_service import UserService
from services.livro_service import LivroService
from datetime import datetime
from models.emprestimo import Emprestimo

emprestimo_service = EmprestimoService()
user_service = UserService()
livro_service = LivroService()

@route('/emprestimos')
def listar_emprestimos():
    require_login()
    usuario_id = int(request.get_cookie("usuario_id"))  # ID real
    emprestimos = emprestimo_service.get_emprestimos_usuario(usuario_id)
    return template('emprestimos.tpl', emprestimos=emprestimos, livros=livro_service.livros)

@route('/emprestimos/novo')
def novo_emprestimo_form():
    require_login()
    livros_disponiveis = [l for l in livro_service.livros if l.disponivel]
    return template('emprestimo_form.tpl', livros=livros_disponiveis)

@route('/emprestimos/criar', method='POST')
def criar_emprestimo():
    require_login()
    usuario_id = int(request.get_cookie("usuario_id"))
    livro_id = int(request.forms.get('livro_id'))
    data_retirada = datetime.today().strftime('%Y-%m-%d')

    novo = Emprestimo(
        id=emprestimo_service.gerar_id(),
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_retirada=data_retirada
    )

    emprestimo_service.adicionar_emprestimo(novo)
    livro_service.marcar_como_indisponivel(livro_id)
    redirect('/emprestimos')

@route('/emprestimos/devolver/<emprestimo_id:int>')
def devolver(emprestimo_id):
    require_login()
    hoje = datetime.today().strftime('%Y-%m-%d')
    emprestimo_service.devolver_livro(emprestimo_id, hoje)
    redirect('/emprestimos')

def require_login():
    if not request.get_cookie("usuario_id"):
        redirect('/login')