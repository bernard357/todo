from bottle import request, response, abort, template

class HtmlView(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def list_items(self, items, filter={}):
        '''Lists items'''

        return template('views/list_items', prefix=self.prefix, items=items)

    def create_item_form(self):
        '''Gets a form to create an item'''

        return template('views/create_item', prefix=self.prefix)

    def create_item(self, params):
        '''Creates an item'''

        raise NotImplementedError()

        response.status = 201
        response.headers['Location'] = self.prefix+'/todo/'+str(item['id'])

    def read_item(self, item):
        '''Reads an item'''

        raise NotImplementedError()

    def update_item_form(self, item):
        '''Gets a form to edit an item'''

        return template('views/update_item', prefix=self.prefix, item=item)

    def update_item(self, item):
        '''Updates an item'''

        raise NotImplementedError()

    def delete_item_form(self, item):
        '''Deletes an item'''

        return template('views/delete_item', prefix=self.prefix, item=item)

    def delete_item(id):
        '''Deletes an item'''

        raise NotImplementedError()

    def error400(self, error):
        response.headers['Cache-Control'] = 'no-cache'
        return 'Bad request'

    def error404(self, error):
        response.headers['Cache-Control'] = 'no-cache'
        return 'Not found'
