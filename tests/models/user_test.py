from datetime import datetime
from unittest import TestCase
from mongoengine import ValidationError, StringField
from models.User import User

__author__ = 'johska'


class UserTest(TestCase):

    def test_user_fields(self):
        user = User(name='Nils', hash='myhash', salt='1213213')

        self.assertTrue(hasattr(user, 'name'))
        self.assertEquals(unicode, type(user.name))

        self.assertTrue(hasattr(user, 'hash'))
        self.assertEquals(unicode, type(user.hash))

        self.assertTrue(hasattr(user, 'salt'))
        self.assertEquals(unicode, type(user.salt))

        self.assertTrue(hasattr(user, 'created'))
        self.assertEquals(datetime, type(user.created))

    def test_user_missing_fields_error(self):
        with self.assertRaises(ValidationError):
            user = User()
            user.validate()

    def test_valid_user(self):
        user = User(name='Nils', hash='myhash', salt='1213213')
        user.validate()
        self.assertIsNotNone(user)
