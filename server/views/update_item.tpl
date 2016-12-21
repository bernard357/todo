% rebase('page.tpl')
%#template for editing a todo
<p>Edit the task with ID = {{ item['id'] }}</p>
<form action="/todo/{{ item['id'] }}" method="post">
  <input type="text" name="task" value="{{ item['task'] }}" size="100" maxlength="100">
  <select name="status">
    <option>open</option>
    <option>closed</option>
  </select>
  <br>
  <input type="submit" name="save" value="save">
</form>
