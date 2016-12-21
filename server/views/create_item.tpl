% rebase('page.tpl')
%#template for the form for a new todo
<p>Add a new task to the ToDo list:</p>
<form action="/todos" method="post">
  <input type="text" size="100" maxlength="100" name="task">
  <input type="submit" name="save" value="save">
</form>
