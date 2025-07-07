% rebase('layout.tpl')

<h2>Lista de Usuários</h2>

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
                <a href="/usuarios/deletar/{{u.id}}" class="btn btn-sm btn-danger" onclick="return confirm('Confirma exclusão do usuário?')">Excluir</a>
            </td>
        </tr>
        % end
    </tbody>
</table>

<a href="/usuarios/novo" class="btn btn-success">+ Adicionar Usuário</a>
