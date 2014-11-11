from unittest import TestCase
from mongoengine import ValidationError
from models.Message import Message

__author__ = 'johska'


class MessageTest(TestCase):

    def test_missing_message_raise_validation_error(self):

        with self.assertRaises(ValidationError):
            message = Message()
            message.validate()

    def test_message_fields(self):
        message = Message()

        self.assertTrue(hasattr(message, 'header'))
        self.assertTrue(hasattr(message, 'message'))
        self.assertTrue(hasattr(message, 'receivers'))
        self.assertTrue(hasattr(message, 'sender'))
"""
    def test_valid_message(self):
        users = []
        users.append(User(name='Nils', hash='myHash', salt='mySalt'))
        users.append(User(name='Stine', hash='myHash2', salt='mySalt2'))
        users.append(User(name='Geir', hash='myHash3', salt='mySalt3'))

        message_text = 'Hallaisen!'
        sender = User(name='Nils', hash='myHash', salt='mySalt')

        message = Message(message=message_text, receivers=users, sender=sender)
        message.validate()
"""