from bottle import route, request, template, redirect
from datetime import datetime
from controllers.auth_controller import require_login
from services.emprestimo import emprestimo_service
from services.user_service import user_service
from services.livro_service import livro_service
from models.emprestimo import Emprestimo

@route('/emprestimos')
@require_login
def listar_emprestimos():
    user_email = request.get_cookie("logged_user", secret='SUA-CHAVE-SECRETA-MUITO-FORTE')
    usuario = user_service.find_user_by_email(user_email)
    
    emprestimos = []
    if usuario:
        emprestimos = emprestimo_service.get_emprestimos_usuario(usuario.id)
    
    livros_emprestados = [livro_service.find_livro_by_id(e.livro_id) for e in emprestimos]

    return template('emprestimos_list.tpl', emprestimos=emprestimos, livros=livros_emprestados, title="Meus Empréstimos")

@route('/emprestimos/novo')
@require_login
def novo_emprestimo_form():
    livros_disponiveis = livro_service.get_livros_disponiveis()
    return template('emprestimo_form.tpl', livros=livros_disponiveis, title="Novo Empréstimo")

@route('/emprestimos/criar', method='POST')
@require_login
def criar_emprestimo():
    user_email = request.get_cookie("logged_user", secret='SUA-CHAVE-SECRETA-MUITO-FORTE')
    usuario = user_service.find_user_by_email(user_email)
    livro_id = int(request.forms.get('livro_id'))
    
    if not usuario:
        return redirect('/login')

    novo_emprestimo = Emprestimo(
        id=None,
        usuario_id=usuario.id,
        livro_id=livro_id,
        data_retirada=datetime.today().strftime('%Y-%m-%d'),
        data_devolucao=None
    )

    emprestimo_service.adicionar_emprestimo(novo_emprestimo)
    livro_service.marcar_como_indisponivel(livro_id)

    redirect('/emprestimos')

@route('/emprestimos/devolver/<emprestimo_id:int>', method='POST')
@require_login
def devolver(emprestimo_id):
    emprestimo = emprestimo_service.find_emprestimo_by_id(emprestimo_id)

    if emprestimo:
        hoje = datetime.today().strftime('%Y-%m-%d')
        emprestimo_service.devolver_livro(emprestimo_id, hoje)
        livro_service.marcar_como_disponivel(emprestimo.livro_id)

    redirect('/emprestimos')