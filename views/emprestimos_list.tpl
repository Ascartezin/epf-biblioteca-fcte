% rebase('layout.tpl', title=title)

<h2>{{ title }}</h2>

<a href="/emprestimos/novo" class="btn btn-primary mb-3">Novo Empréstimo</a>

<table class="table table-striped">
    <thead>
        <tr>
            <th>Livro</th>
            <th>Data de Retirada</th>
            <th>Ação</th>
        </tr>
    </thead>
    <tbody>
        % if not emprestimos:
            <tr>
                <td colspan="3" class="text-center">Nenhum empréstimo ativo.</td>
            </tr>
        % end
        % for i, emprestimo in enumerate(emprestimos):
            <tr>
                <td>{{ livros[i].titulo if i < len(livros) else 'Livro não encontrado' }}</td>
                <td>{{ emprestimo.data_retirada }}</td>
                <td>
                    <form action="/emprestimos/devolver/{{emprestimo.id}}" method="post" style="display:inline;">
                        <button type="submit" class="btn btn-sm btn-success">Devolver</button>
                    </form>
                </td>
            </tr>
        % end
    </tbody>
</table>