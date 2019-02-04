# -*- coding:utf-8 -*-
__author__ = 'Gvammer'

from eve import Eve
from eve.auth import BasicAuth
from settings import ADMIN_USERNAME, ADMIN_PASSWORD
from eve.auth import requires_auth

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

def get_distance_price(distance):
    return 100 * (float(distance) / 1000.0)


def before_insert(resource_name, documents):

    if resource_name == 'drivings':
        for doc in documents:
            if doc['distance']:
                doc['cost'] = get_distance_price(doc['distance'])

    if resource_name == 'user':
        for doc in documents:
            if doc['driver_licence_number']:
                doc['is_driver'] = True


app = Eve(auth=MyBasicAuth)
app.on_insert += before_insert


@app.route('/get_price')
@requires_auth(MyBasicAuth)
def get_price():
    from flask import request
    distance = float(request.args.get('distance', 0))
    return str(get_distance_price(distance))


if __name__ == '__main__':
    app.run(host="0.0.0.0")