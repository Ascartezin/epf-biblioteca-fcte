% rebase('layout.tpl', title=title)

<h2>{{ title }}</h2>

% if erro:
<div class="alert alert-danger">
    {{ erro }}
</div>
% end

<form action="{{ '/livros/atualizar' if livro else '/livros/criar' }}" method="post">

    % if livro:
        <input type="hidden" name="id" value="{{ livro.id }}">
    % end

    <div class="mb-3">
        <label for="titulo" class="form-label">Título:</label>
        <input type="text" name="titulo" id="titulo" class="form-control" 
               value="{{ livro.titulo if livro else '' }}" required>
    </div>

    <div class="mb-3">
        <label for="autor" class="form-label">Autor:</label>
        <input type="text" name="autor" id="autor" class="form-control" 
               value="{{ livro.autor if livro else '' }}" required>
    </div>

    <button type="submit" class="btn btn-primary">{{ 'Atualizar' if livro else 'Adicionar' }}</button>
    <a href="/livros" class="btn btn-secondary">Cancelar</a>
</form>