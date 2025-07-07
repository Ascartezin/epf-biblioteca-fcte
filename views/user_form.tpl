% rebase('layout.tpl')

% is_edicao = usuario and (usuario.get('id') if isinstance(usuario, dict) else usuario.id)

<h2>{{ 'Editar Usuário' if is_edicao else 'Novo Usuário' }}</h2>

% if erro:
    <div class="alert alert-danger">{{ erro }}</div>
% end

<form method="post" action="{{ '/usuarios/atualizar' if is_edicao else '/usuarios/criar' }}">
    % if is_edicao:
        <input type="hidden" name="id" value="{{ usuario.get('id') if isinstance(usuario, dict) else usuario.id }}">
    % end

    <div class="mb-3">
        <label for="name" class="form-label">Nome</label>
        <input type="text" id="name" name="name" required class="form-control"
               value="{{ usuario.get('name') if isinstance(usuario, dict) else usuario.name }}">
    </div>

    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" id="email" name="email" required class="form-control"
               value="{{ usuario.get('email') if isinstance(usuario, dict) else usuario.email }}">
    </div>

    <div class="mb-3">
        <label for="birthdate" class="form-label">Data de nascimento</label>
        <input type="date" id="birthdate" name="birthdate" required class="form-control"
               value="{{ usuario.get('birthdate') if isinstance(usuario, dict) else usuario.birthdate }}">
    </div>

    <div class="mb-3">
        <label for="senha" class="form-label">Senha</label>
        <input type="password" id="senha" name="senha" class="form-control"
               {{ '' if is_edicao else 'required' }}>
        % if is_edicao:
            <div class="form-text">Deixe em branco para manter a senha atual.</div>
        % end
    </div>

    <button type="submit" class="btn btn-primary">
        {{ 'Atualizar' if is_edicao else 'Cadastrar' }}
    </button>
    <a href="/usuarios" class="btn btn-secondary">Cancelar</a>
</form>
