from bottle import request, redirect

def require_login():
    """Middleware para proteger rotas: redireciona para login se não autenticado."""
    if not request.get_cookie("user"):
        redirect('/login')
