% rebase('layout.tpl')

<h2>Login</h2>

% # Esta condição agora verifica se a variável 'erro' existe antes de usá-la.
% if 'erro' in locals() and erro:
    <div class="alert alert-danger">{{ erro }}</div>
% end

<form method="post" action="/login">
    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" id="email" name="email" required class="form-control">
    </div>

    <div class="mb-3">
        <label for="senha" class="form-label">Senha</label>
        <input type="password" id="senha" name="senha" required class="form-control">
    </div>

    <button type="submit" class="btn btn-primary">Entrar</button>
</form>