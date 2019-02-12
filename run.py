# -*- coding:utf-8 -*-
__author__ = 'Gvammer'

from eve import Eve
from eve.auth import BasicAuth
from settings import ADMIN_USERNAME, ADMIN_PASSWORD
from eve.auth import requires_auth
from eve.methods.post import post_internal
from eve.methods.put import put_internal
from eve.methods.common import get_document
import json

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

def get_distance_price(distance):
    return 100 * (float(distance) / 1000.0)


def before_update(resource_name, item, payload):

    if resource_name == 'drivings':
        driving = json.loads(item.get_data())

        if 'driver' in driving and driving['driver'] == 'CLEAN':
            original = get_document(resource_name, False, **{"_id": payload['_id']})
            new = {}
            for k in original:
                new[k] = original[k]

            new['customer'] = str(new['customer'])
            del new['_created']
            del new['driver']
            del new['_updated']
            del new['_etag']
            del new['_id']

            del driving['driver']

            for k in driving:
                new[k] = driving[k]

            return put_internal(resource_name, new, False, True, **{"_id": payload['_id']})
            # app.data.replace(resource_name, original['_etag'], new, original)




def after_insert(resource_name, request, payload):
    if resource_name == 'drivings':
        for doc in [request.get_data()]:
            doc = json.loads(doc)

            if doc['destinations']:
                destinations = json.loads(doc['destinations'])

                for dest in destinations:
                    dest['driving'] = json.loads(payload.get_data())['_id']

                    print post_internal('destinations', payl=dest)

                del doc['destinations']

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
app.on_post_POST += after_insert
app.on_pre_PATCH += before_update



@app.route('/get_price')
@requires_auth(MyBasicAuth)
def get_price():
    from flask import request
    distance = float(request.args.get('distance', 0))
    return str(get_distance_price(distance))


if __name__ == '__main__':
    app.run(host="0.0.0.0")