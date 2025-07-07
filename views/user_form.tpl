% rebase('layout.tpl', title=title)

% if erro:
<div class="alert alert-danger">
    {{ erro }}
</div>
% end

<form action="{{ '/usuarios/atualizar' if (usuario and hasattr(usuario, 'id')) else '/usuarios/criar' }}" method="post">

    % # A condição agora verifica se 'usuario' existe E se ele possui o atributo 'id'
    % if usuario and hasattr(usuario, 'id') and usuario.id:
        <input type="hidden" name="id" value="{{ usuario.id }}">
    % end

    <div class="mb-3">
        <label for="name" class="form-label">Nome:</label>
        <input type="text" name="name" id="name" class="form-control" 
               value="{{ usuario.name if usuario else '' }}" required>
    </div>

    <div class="mb-3">
        <label for="email" class="form-label">E-mail:</label>
        <input type="email" name="email" id="email" class="form-control" 
               value="{{ usuario.email if usuario else '' }}" required>
    </div>

    <div class="mb-3">
        <label for="birthdate" class="form-label">Data de Nascimento:</label>
        <input type="date" name="birthdate" id="birthdate" class="form-control"
               value="{{ usuario.birthdate if usuario else '' }}" required>
    </div>

    <div class="mb-3">
        <label for="senha" class="form-label">Senha:</label>
        <input type="password" name="senha" id="senha" class="form-control" 
               placeholder="{{ 'Deixe em branco para não alterar' if (usuario and hasattr(usuario, 'id')) else '' }}">
        % if not (usuario and hasattr(usuario, 'id')):
        <small class="form-text text-muted">A senha é obrigatória para novos usuários.</small>
        % end
    </div>

    <button type="submit" class="btn btn-primary">{{ 'Atualizar' if (usuario and hasattr(usuario, 'id')) else 'Criar' }}</button>
    <a href="/usuarios" class="btn btn-secondary">Cancelar</a>
</form>