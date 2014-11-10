import datetime
from mongoengine import Document, StringField, DateTimeField

__author__ = 'johska'


class User(Document):

    meta = {
        'collection': 'users'
    }

    name = StringField(required=True)
    hash = StringField(required=True)
    salt = StringField(required=True)
    created = DateTimeField(required=True, default=datetime.datetime.now())