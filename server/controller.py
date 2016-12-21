import json
import sqlite3

from bottle import route, run, debug, template, static_file, error, abort
from bottle import request, response
from bottle import post, get, put, delete

# only needed when you run Bottle on mod_wsgi
from bottle import default_app

from model import TodoModel

from view_json import JsonView
from view_html import HtmlView

@get('/todos/index')
def index_all():
    '''Lists items'''

    items = model.list()

    view = HtmlView(prefix())
    return view.list_items(items)

@get('/todos/index-active')
def index_active():
    '''Lists items'''

    filter = {
        'status': '1',
    }
    items = model.list(filter)

    view = HtmlView(prefix())
    return view.list_items(items, filter)

@get('/todos/index-closed')
def index_closed():
    '''Lists items'''

    filter = {
        'status': '0',
    }
    items = model.list(filter)

    view = HtmlView(prefix())
    return view.list_items(items, filter)

@get('/todos')
def list_todos():
    '''Lists items'''

    items = model.list()

    view = JsonView(prefix())
    return view.list_items(items)

@get('/todos/active')
def list_active_todos():
    '''Lists items'''

    filter = {
        'status': '1',
    }
    items = model.list(filter)

    view = JsonView(prefix())
    return view.list_items(items, filter)

@get('/todos/closed')
def list_closed_todos():
    '''Lists items'''

    filter = {
        'status': '0',
    }
    items = model.list(filter)

    view = JsonView(prefix())
    return view.list_items(items, filter)

@get('/todo/create')
def create_todo_form():
    '''Gets a form to create an item'''

    view = HtmlView(prefix())
    return view.create_item_form()

@post('/todos')
def create_todo():
    '''Creates an item'''

    item = model.create(request.params)

    response.status = 201
    response.headers['Location'] = prefix()+'/todo/'+str( item['id'] )

    view = JsonView(prefix())
    return view.create_item(item)

@get('/todo/<id:int>')
def get_todo(id):
    '''Reads an item'''

    item = model.read(id)

    view = JsonView(prefix())
    return view.read_item(item)

@get('/todo/update-<id:int>')
def update_todo_form(id):
    '''Gets a form to edit an item'''

    item = model.read(id)

    view = HtmlView(prefix())
    return view.update_item_form(item)

@post('/todo/<id:int>')
def update_todo(id):
    '''Updates an item'''

    item = model.update(id, request.params)

    view = JsonView(prefix())
    return view.update_item(item)

@get('/todo/delete-<id:int>')
def delete_todo_form(id):
    '''Deletes an item'''

    item = model.read(id)

    view = HtmlView(prefix())
    return view.delete_item_form(item)

@post('/todo/delete-<id:int>')
def delete_todo(id):
    '''Deletes an item'''

    item = model.delete(id)

    view = JsonView(prefix())
    return view.delete_item(item)

@get('/assets/<filename:path>')
def serve_asset(filename):
    print('serving {}'.format(filename))
    return static_file(filename, root='./assets')

@error(400)
def error400(error):
    view = JsonView(prefix())
    return view.error400(error)

@error(404)
def error404(error):
    view = JsonView(prefix())
    return view.error404(error)

def prefix():
    return request.urlparts.scheme+'://'+request.urlparts.netloc

model = TodoModel()
model.setup()

debug(True)
run(reloader=True)
# remember to remove reloader=True and debug(True) when you move your
# application from development to a productive environment