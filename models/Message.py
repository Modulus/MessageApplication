from mongoengine import Document, StringField, ListField, EmbeddedDocumentField
from app.models.User import User

__author__ = 'johska'


class Message(Document):
    meta = {
        'collection': 'messages'
    }
    header = StringField(required=False, max_length=128)
    mesage = StringField(required=True, max_length=512, min_length=1)
    receiver = ListField(EmbeddedDocumentField(document_type=User, required=False))
    sender = StringField(required=True)


