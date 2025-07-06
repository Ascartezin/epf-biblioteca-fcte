% rebase('layout.tpl')
<h2>Meus Empréstimos</h2>

<a class="btn btn-primary" href="/emprestimos/novo">Novo Empréstimo</a>
<br><br>

<table class="table table-bordered">
    <thead>
        <tr>
            <th>Livro</th>
            <th>Data de Retirada</th>
            <th>Data de Devolução</th>
            <th>Ação</th>
        </tr>
    </thead>
    <tbody>
    % for e in emprestimos:
        <tr>
            <td>
                % for livro in livros:
                    % if livro.id == e.livro_id:
                        {{livro.titulo}} - {{livro.autor}}
                    % end
                % end
            </td>
            <td>{{e.data_retirada}}</td>
            <td>
                % if e.data_devolucao:
                    {{e.data_devolucao}}
                % else:
                    <span class="text-warning">Em aberto</span>
                % end
            </td>
            <td>
                % if not e.data_devolucao:
                    <a class="btn btn-sm btn-success" href="/emprestimos/devolver/{{e.id}}">Devolver</a>
                % else:
                    <span class="text-muted">Finalizado</span>
                % end
            </td>
        </tr>
    % end
    </tbody>
</table>
