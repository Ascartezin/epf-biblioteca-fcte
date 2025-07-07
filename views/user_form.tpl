% rebase('layout.tpl')

<h2>Cadastrar Novo Usuário</h2>

<form method="post" action="/usuarios/criar" class="mt-4">
    <div class="mb-3">
        <label for="id" class="form-label">ID:</label>
        <input type="number" name="id" id="id" class="form-control" required>
    </div>

    <div class="mb-3">
        <label for="name" class="form-label">Nome:</label>
        <input type="text" name="name" id="name" class="form-control" required>
    </div>

    <div class="mb-3">
        <label for="email" class="form-label">E-mail:</label>
        <input type="email" name="email" id="email" class="form-control" required>
    </div>

    <div class="mb-3">
        <label for="birthdate" class="form-label">Data de Nascimento:</label>
        <input type="date" name="birthdate" id="birthdate" class="form-control" required>
    </div>

    <button type="submit" class="btn btn-success">Cadastrar</button>
    <a href="/usuarios" class="btn btn-secondary">Cancelar</a>
</form>
