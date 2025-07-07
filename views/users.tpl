% rebase('layout.tpl')

<h2>Lista de Usuários</h2>

<a href="/usuarios/novo" class="btn btn-primary mb-3">Adicionar Usuário</a>

<table class="table table-striped">
    <thead>
        <tr>
            <th>Nome</th>
            <th>Email</th>
            <th>Data de Nascimento</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
        % for u in usuarios:
        <tr>
            <td>{{u.name}}</td>
            <td>{{u.email}}</td>
            <td>{{u.birthdate}}</td>
            <td>
                <a href="/usuarios/editar/{{u.id}}" class="btn btn-sm btn-primary">Editar</a>

                <form action="/usuarios/deletar/{{u.id}}" method="post" style="display:inline;">
                    <button type="submit" class="btn btn-sm btn-danger" onclick="return confirm('Confirma exclusão do usuário?');">Excluir</button>
                </form>
            </td>
        </tr>
        % end
        % if not usuarios:
        <tr>
            <td colspan="4" class="text-center">Nenhum usuário cadastrado.</td>
        </tr>
        % end
    </tbody>
</table>