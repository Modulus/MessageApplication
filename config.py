__author__ = 'johska'


class ProdConfig(object):
    MONGODB_SETTINGS = {'db': 'MessageApplication', 'host': '127.0.0.1'}


class TestConfig(object):
    MONGODB_SETTINGS = {'db': 'MessageApplicationTestBase', 'host': '127.0.0.1'}