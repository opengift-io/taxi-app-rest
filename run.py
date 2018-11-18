# -*- coding:utf-8 -*-
__author__ = 'Gvammer'

from eve import Eve
from eve.auth import BasicAuth
from settings import ADMIN_USERNAME, ADMIN_PASSWORD

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

app = Eve(auth=MyBasicAuth)

if __name__ == '__main__':
    app.run()