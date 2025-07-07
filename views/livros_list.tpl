% rebase('layout.tpl', title=title)

<h2>{{ title }}</h2>

<table class="table table-striped">
    <thead>
        <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Autor</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        % for livro in livros:
            <tr>
                <td>{{ livro.id }}</td>
                <td>{{ livro.titulo }}</td>
                <td>{{ livro.autor }}</td>
                <td>
                    % if livro.disponivel:
                        <span class="badge bg-success">Disponível</span>
                    % else:
                        <span class="badge bg-danger">Indisponível</span>
                    % end
                </td>
            </tr>
        % end
    </tbody>
</table>