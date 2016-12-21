% rebase('page.tpl')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The items are as follows:</p>
<div class="table-responsive">
<table class="table">
%for item in items:
  <tr>
  %for key in item:
    <td>{{ item[ key ] }}</td>
  %end
    <td><a href="{{ prefix }}/todo/update-{{ item['id'] }}">update</a></td>
    <td><a href="{{ prefix }}/todo/delete-{{ item['id'] }}">delete</a></td>
  </tr>
%end
</table>
</div>
