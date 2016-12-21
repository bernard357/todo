
from bottle import abort
import logging

import sqlite3

class TodoModel(object):

    def setup(self):

        db = sqlite3.connect('todo.db')

        db.execute("DROP TABLE IF EXISTS todo")

        db.execute(
            ( "CREATE TABLE todo ("
              "id INTEGER PRIMARY KEY, "
              "task char(100) NOT NULL, "
              "status bool NOT NULL)" ) )

        items = [
            ('Read A-byte-of-python to get a good introduction into Python',0),
            ('Visit the Python website',1),
            ('Test various editors for and check the syntax highlighting',1),
            ('Choose your favorite WSGI-Framework',0),
        ]
        for item in items:
            db.execute(self.insert(), item)

        db.commit()

    def insert(self):
        return "INSERT INTO todo (task,status) VALUES (?, ?)"

    def list(self, filter={}):

        likes = []
        for key in filter.keys():
            likes.append( key+" LIKE '{}'".format(filter[key]) )

        where = ''
        if len(likes) > 0:
            where = ' WHERE '+' AND '.join(likes)

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT id, task, status FROM todo" + where)
        result = c.fetchall()
        c.close()
        return self._to_items(result)

    def create(self, params):

        required = ['task']
        self._require(required, params)

        task = params.get('task', '').strip()

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute(self.insert(), (task, 1))
        id = c.lastrowid
        conn.commit()
        c.close()

        return self.read(id)

    def read(self, id):

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT id, task, status FROM todo WHERE id LIKE ?", (id,))
        result = c.fetchall()
        c.close()
        if len(result) < 1:
            abort(404)

        return self._to_item(result[0])

    def update(self, id, params):

        required = ['task', 'status']
        self._require(required, params)

        task = params.get('task', '').strip()
        status = params.get('status', '').strip()
        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute(
            "UPDATE todo SET task = ?, status = ? WHERE id LIKE ?",
            (task, status, id))
        conn.commit()
        c.close()

        return self.read(id)

    def delete(self, id):

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("DELETE FROM todo WHERE id LIKE?", (id,))
        changed = conn.total_changes()
        conn.commit()
        c.close()

        print(changed)
        if changed < 1:
            abort(404)

    def _to_items(self, records):

        items = []
        for record in records:
            items.append(self._to_item(record))
        return items

    def _to_item(self, record):

        item = {}
        item['id'] = record[0]
        item['task'] = record[1]
        item['status'] = record[2]
        return item

    def _require(self, keys, params):

        for key in keys:
            if key not in params:
                logging.error("missing parameter '{}'".format(key))
                abort(400)
