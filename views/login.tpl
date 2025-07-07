% rebase('layout.tpl')

<h2>Login</h2>

<form action="/login" method="post" class="login-form">
  <div class="form-group">
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required>
  </div>

  <div class="form-group">
    <label for="birthdate">Data de nascimento:</label><br>
    <input type="date" id="birthdate" name="birthdate" required>
  </div>

  <button type="submit">Entrar</button>
</form>
