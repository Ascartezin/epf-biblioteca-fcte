% rebase('layout.tpl')

<h2>📚 Lista de Livros</h2>

<table class="livros-table">
  <thead>
    <tr>
      <th>ID</th>
      <th>Título</th>
      <th>Autor</th>
      <th>Ações</th>
    </tr>
  </thead>
  <tbody>
    % for livro in livros:
      <tr>
        <td>{{livro.id}}</td>
        <td>{{livro.titulo}}</td>
        <td>{{livro.autor}}</td>
        <td>
          <a class="btn editar" href="/livros/{{livro.id}}/edit">Editar</a>
          <a class="btn excluir" href="/livros/{{livro.id}}/delete" onclick="return confirm('Tem certeza que deseja excluir este livro?')">Excluir</a>
        </td>
      </tr>
    % end
  </tbody>
</table>

<div style="margin-top: 20px;">
  <a class="btn adicionar" href="/livros/novo">➕ Adicionar novo livro</a>
</div>
