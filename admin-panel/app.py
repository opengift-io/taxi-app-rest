import datetime

from flask import Flask, redirect

import flask_admin as admin
from flask_mongoengine import MongoEngine
from flask_admin.form import rules
from flask_admin.contrib.mongoengine import ModelView

# Create application
app = Flask(__name__, static_url_path='/static')

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'
app.config['MONGODB_SETTINGS'] = {
    'DB': 'taxi',
    'host': 'mongodb://taxi:UffX8g8f@127.0.0.1:27017/taxi'
}

# Create models
db = MongoEngine()
db.init_app(app)


class car_brands(db.Document):
    title = db.StringField(max_length=400)
    code = db.StringField()
    logo = db.FileField(default=False)
    _updated = db.DateTimeField()
    _etag = db.StringField(max_length=300)

    # Required for administrative interface
    def __unicode__(self):
        return self.title

class car_models(db.Document):
    title = db.StringField(max_length=400)
    code = db.StringField()
    picture = db.FileField(default=False)
    brand = db.ReferenceField(car_brands, required=False)
    _updated = db.DateTimeField()
    _etag = db.StringField(max_length=300)

    # Required for administrative interface
    def __unicode__(self):
        return self.title

class car_colors(db.Document):
    title = db.StringField(max_length=400)
    code = db.StringField()
    picture = db.FileField(default=False)
    _updated = db.DateTimeField()
    _etag = db.StringField(max_length=300)

    # Required for administrative interface
    def __unicode__(self):
        return self.title

# Define mongoengine documents
class Users(db.Document):
    firstname = db.StringField(max_length=100)
    lastname = db.StringField(max_length=100)
    email = db.StringField(max_length=100)
    phone = db.StringField(max_length=100)
    password = db.StringField(max_length=40)
    driver_car_licence_plate_number = db.StringField(max_length=30)
    driver_licence_number = db.StringField(max_length=30)
    driver_licence_end_date = db.StringField(max_length=30)
    location = db.StringField(max_length=30)
    born = db.StringField(max_length=30)
    is_driver = db.BooleanField(default=False)
    licence_front = db.ImageField()
    licence_back = db.ImageField()
    avatar = db.ImageField()
    _updated = db.DateTimeField()
    _etag = db.StringField(max_length=300)
    driver_car_color = db.ReferenceField(car_colors, required=False)
    driver_car_model = db.ReferenceField(car_models, required=False)

    driver_ownership_doc_number = db.StringField(max_length=300)
    car_ownership_doc = db.ImageField()

    def __unicode__(self):
        return self.firstname

class Drivings(db.Document):
    address_from = db.StringField(max_length=500)
    address_to = db.StringField(max_length=500)
    location_from_lat = db.FloatField()
    location_from_lng = db.FloatField()
    location_to_lat = db.FloatField()
    location_to_lng = db.FloatField()
    driver_location_lat = db.FloatField()
    driver_location_lng = db.FloatField()
    distance = db.FloatField(required=False)
    eta_driver_time = db.FloatField(required=False)
    customer = db.ReferenceField(Users)
    driver = db.ReferenceField(Users, required=False)
    cost = db.DecimalField(required=False)
    duration = db.DecimalField(required=False)
    children_qty = db.DecimalField(required=False)
    comment = db.StringField(required=False, max_length=1000)
    destinations = db.StringField(required=False, max_length=1000)
    status = db.StringField(max_length=30)
    _updated = db.DateTimeField()
    _etag = db.StringField(max_length=300)



    def __unicode__(self):
        return self.address_from
#
#

# 'car_brands': {
#         'schema': {
#             'title': {
#                 'type': 'string',
#                 'minlength': 1,
#                 'maxlength': 400,
#                 'required': True,
#             },
#             'code': {
#                 'type': 'string',
#                 'minlength': 1,
#                 'maxlength': 50,
#                 'required': True,
#             },
#             'logo': {
#                 'type': 'media'
#             }
#         }
#     },
#     'car_models': {
#         'schema': {
#             'title': {
#                 'type': 'string',
#                 'minlength': 1,
#                 'maxlength': 400,
#                 'required': True,
#             },
#             'code': {
#                 'type': 'string',
#                 'minlength': 1,
#                 'maxlength': 50,
#                 'required': True,
#             },
#             'picture': {
#                 'type': 'media'
#             },
#             'brand': {
#                 'type': 'objectid',
#                 'data_relation': {
#                     'resource': 'car_brands',
#                     'field': '_id',
#                     'embeddable': True
#                 }
#             },
#         }
#     },
#     'car_colors': {
#         'schema': {
#             'title': {
#                 'type': 'string',
#                 'minlength': 1,
#                 'maxlength': 400,
#                 'required': True,
#             },
#             'code': {
#                 'type': 'string',
#                 'minlength': 1,
#                 'maxlength': 50,
#                 'required': True,
#             },
#             'picture': {
#                 'type': 'media'
#             }
#         }
#     }


#
#
# class Tag(db.Document):
#     name = db.StringField(max_length=10)
#
#     def __unicode__(self):
#         return self.name
#
#
# class Comment(db.EmbeddedDocument):
#     name = db.StringField(max_length=20, required=True)
#     value = db.StringField(max_length=20)
#     tag = db.ReferenceField(Tag)
#
#
# class Post(db.Document):
#     name = db.StringField(max_length=20, required=True)
#     value = db.StringField(max_length=20)
#     inner = db.ListField(db.EmbeddedDocumentField(Comment))
#     lols = db.ListField(db.StringField(max_length=20))
#
#
# class File(db.Document):
#     name = db.StringField(max_length=20)
#     data = db.FileField()
#
#
# class Image(db.Document):
#     name = db.StringField(max_length=20)
#     image = db.ImageField(thumbnail_size=(100, 100, True))


# Customized admin views
class UserView(ModelView):
    column_filters = ['email']

    column_searchable_list = ('email', 'password')

    # form_ajax_refs = {
    #     'tags': {
    #         'fields': ('name',)
    #     }
    # }

class DrivingsView(ModelView):
    column_filters = ['address_to']

    column_searchable_list = ('address_from', 'address_to')


class TodoView(ModelView):
    column_filters = ['done']

    form_ajax_refs = {
        'user': {
            'fields': ['name']
        }
    }


class PostView(ModelView):
    form_subdocuments = {
        'inner': {
            'form_subdocuments': {
                None: {
                    # Add <hr> at the end of the form
                    'form_rules': ('name', 'tag', 'value', rules.HTML('<hr>')),
                    'form_widget_args': {
                        'name': {
                            'style': 'color: red'
                        }
                    }
                }
            }
        }
    }

# Flask views
@app.route('/')
def index():
    return redirect('/static/app.html')


if __name__ == '__main__':
    # Create admin
    admin = admin.Admin(app, 'Xpress Taxi', template_mode="bootstrap3")

    # Add views
    admin.add_view(UserView(Users))
    admin.add_view(DrivingsView(Drivings))
    # admin.add_view(ModelView(Tag))
    # admin.add_view(PostView(Post))
    # admin.add_view(ModelView(File))
    # admin.add_view(ModelView(Image))

    # Start app
    app.run(debug=True, port=80, host="0.0.0.0")
