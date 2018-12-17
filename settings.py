# -*- coding:utf-8 -*-
from settings_local import *

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    # Описываем ресурс `/users`
    'users': {
        # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
        # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
        # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
        'schema': {
            'firstname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 10,
                'required': True,
            },
            'lastname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
                'required': False,
            },
            'email': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 200,
                'required': True,
                'unique': True,
            },
            'phone': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 200,
                'required': True,
            },
            'password': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 200,
                'required': True,
            },
            'role': {
                'type': 'list', # тип: список
                'allowed': ["driver", "contributor"], # разрешаем использовать значения: "author", "contributor"
            },
            'location': {
                'type': 'dict', # тип: словарь
                # описываем "схему" словаря
                'schema': {
                    'address': {'type': 'string'},
                    'city': {'type': 'string'}
                },
            },
            'born': {
                'type': 'datetime',
            },
            'is_driver': {
                'type': 'boolean',
                'default': True
            }
        }
    },
    'drivings': {
        'schema': {
            'address_from': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 400,
                'required': True,
            },
            'address_to': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 400,
                'required': True,
            },
            'location_from_lot': {
                'type': 'float',
                'required': True,
            },
            'location_to_lat': {
                'type': 'float',
                'required': True,
            },
            'location_from_lon': {
                'type': 'float',
                'required': True,
            },
            'location_to_lon': {
                'type': 'float',
                'required': True,
            },
            'distance': {
                'type': 'float',
                'required': False,
            },
            'customer': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'users',
                    'field': '_id',
                    'embeddable': True
                }
            },
            'driver': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'users',
                    'field': '_id',
                    'embeddable': True
                }
            },
            'cost': {
                'type': 'integer'
            },
            'children_qty': {
                'type': 'integer'
            },
            'comment': {
                'type': 'string',
                'maxlength': 1000,
            }
        }
    },
    'countries': {
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 400,
                'required': True,
            },
            'code': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 3,
                'required': True,
            },
            'flag': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 500,
                'required': True,
            },
        }
    },
    'cities': {
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 400,
                'required': True,
            },
            'code': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 50,
                'required': True,
            },
            'country': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'countries',
                    'field': '_id',
                    'embeddable': True
                }
            },
        }
    }
}

MONGO_QUERY_BLACKLIST = ['$where']