from bottle import request, response, abort
import json

class JsonView(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def list_items(self, items, filter={}):
        '''Lists items'''

        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        return json.dumps(
            [{'todos': list(items)},
             {'filter': filter},
             {'links': self.list_links([('create', 'create')])}])

    def create_item(self, item):
        '''Creates an item'''

        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        return json.dumps(
            [{'todo': item},
             {'result': 'created'},
             {'links': self.list_links( self.get_item_links( item['id'] ) )}])

    def read_item(self, item):
        '''Reads an item'''

        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        return json.dumps(
            [{'todo': item},
             {'result': 'read'},
             {'links': self.list_links( self.get_item_links( item['id'] ) )}])

    def update_item(self, item):
        '''Updates an item'''

        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        return json.dumps(
            [{'todo': item},
             {'result': 'updated'},
             {'links': self.list_links( self.get_item_links( item['id'] ) )}])

    def delete_item(self, item):
        '''Deletes an item'''

        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        return json.dumps(
            [{'result': 'deleted'},
             {'links': self.list_links([('todos', 'todos')])}])

    def error400(self, error):
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        return json.dumps({'error': 'bad request'})

    def error404(self, error):
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        return json.dumps({'error': 'not found'})

    def get_item_links(self, id):
        tuples = []
        tuples.append( ('update', 'update-'+str(id)) )
        tuples.append( ('delete', 'delete-'+str(id)) )
        return tuples

    def list_links(self, items):
        links = []
        for item in items:
            links.append({ item[0]: self.prefix+'/todo/'+item[1] })
        return links
