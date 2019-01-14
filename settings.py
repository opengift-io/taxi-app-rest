# -*- coding:utf-8 -*-
from settings_local import *

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
DATE_FORMAT = "%Y-%d-%m %H:%M:%S"
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
            'avatar': {
                'type': 'media'
            },
            'licence_front': {
                'type': 'media'
            },
            'licence_back': {
                'type': 'media'
            },
            'car_ownership_doc': {
                'type': 'media'
            },
            'driver_licence_number': {
                'type': 'string',
                'maxlength': 20,
            },
            'driver_licence_end_date': {
                'type': 'datetime'
            },
            'driver_ownership_doc_number': {
                'type': 'string',
                'maxlength': 20,
            },
            'driver_car_licence_plate_number': {
                'type': 'string',
                'maxlength': 20,
            },
            'driver_car_model': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'car_models',
                    'field': '_id',
                    'embeddable': True
                }
            },
            'driver_car_color': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'car_colors',
                    'field': '_id',
                    'embeddable': True
                }
            },
            'password': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 200,
                'required': True,
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
                'default': False
            }
        }
    },
    'driving_offers': {
        'schema': {
            'address_to': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 400
            },
            'amount': {
                'type': 'float'
            },
            'driving': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'drivings',
                    'field': '_id',
                    'embeddable': True
                }
            },
            'confirmed_by_customer': {
                'type': 'boolean',
                'default': False
            },
            'confirmed_by_driver': {
                'type': 'boolean',
                'default': False
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
            'location_from_lat': {
                'type': 'float',
                'required': True,
            },
            'location_to_lat': {
                'type': 'float',
                'required': True,
            },
            'location_from_lng': {
                'type': 'float',
                'required': True,
            },
            'location_to_lng': {
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
            'duration': {
                'type': 'integer'
            },
            'children_qty': {
                'type': 'integer'
            },
            'comment': {
                'type': 'string',
                'maxlength': 1000,
            },
            'status': {
                'type': 'string',
                'maxlength': 30,
                'default': 'new'
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
    },
    'car_brands': {
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
            'logo': {
                'type': 'media'
            }
        }
    },
    'car_models': {
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
            'picture': {
                'type': 'media'
            },
            'brand': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'car_brands',
                    'field': '_id',
                    'embeddable': True
                }
            },
        }
    },
    'car_colors': {
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
            'picture': {
                'type': 'media'
            }
        }
    }
}

MONGO_QUERY_BLACKLIST = ['$where']