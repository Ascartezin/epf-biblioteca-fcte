<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">📚 Biblioteca</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Alternar navegação">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item"><a class="nav-link" href="/usuarios">Usuários</a></li>
                    <li class="nav-item"><a class="nav-link" href="/usuarios/novo">+ Adicionar Usuário</a></li>
                    <li class="nav-item"><a class="nav-link" href="/emprestimos">Meus Empréstimos</a></li>
                    <li class="nav-item"><a class="nav-link" href="/emprestimos/novo">Novo Empréstimo</a></li>
                </ul>
                <ul class="navbar-nav ms-auto">
                    % if request.get_cookie("logged_user"):
                        <li class="nav-item">
                            <span class="nav-link">Olá, {{request.get_cookie("logged_user")}}</span>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/logout">Sair</a>
                        </li>
                    % else:
                        <li class="nav-item">
                            <a class="nav-link" href="/login">Entrar</a>
                        </li>
                    % end
                </ul>
            </div>
        </div>
    </nav>

    <main class="container">
        {{!base}}
    </main>

    <footer class="text-center text-muted mt-4 mb-3">
        <small>Projeto OO • Engenharia de Software - UnB Gama</small>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
