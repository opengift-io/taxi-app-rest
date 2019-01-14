# -*- coding:utf-8 -*-
__author__ = 'Gvammer'

from eve import Eve
from eve.auth import BasicAuth
from settings import ADMIN_USERNAME, ADMIN_PASSWORD

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD


def before_insert(resource_name, documents):
    print resource_name
    if resource_name == 'drivings':
        for doc in documents:
            if doc['distance']:
                doc['cost'] = 6 * (float(doc['distance']) / 5000.0)


app = Eve(auth=MyBasicAuth)
app.on_insert += before_insert
if __name__ == '__main__':
    app.run(host="0.0.0.0")