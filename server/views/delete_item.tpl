% rebase('page.tpl')
%#template for confirmation of delete
<p>Are you sure you want to delete following todo?</p>
<p>{{ item['task'] }}</p>
<form action="/todo/delete" method="post">
  <input type="hidden" value="{{ item['id'] }}" name="task">
  <input type="submit" name="save" value="Yes">
</form>
