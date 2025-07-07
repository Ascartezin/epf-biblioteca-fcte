<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adicionar Novo Livro</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Adicionar Novo Livro</h1>

        % if defined('erro') and erro:
            <p class="error">{{erro}}</p>
        % endif

        <form action="/livros/novo" method="post">
            <div class="form-group">
                <label for="nome">Nome do Livro:</label>
                <input type="text" id="nome" name="nome" required value="{{nome or ''}}">
            </div>

            <div class="form-group">
                <label for="autor">Autor:</label>
                <input type="text" id="autor" name="autor" required value="{{autor or ''}}">
            </div>

            <button type="submit">Salvar Livro</button>
        </form>
    </div>
</body>
</html>