__author__ = 'johska'

from MessageApplication import app

from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.httpserver import  HTTPServer

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()

#
# import tornado
# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop
#
#
# #Host this application on the Tornado web server
# def main():
#     server = HTTPServer(app)
#     server.bind(5000)
#     server.start(0)
#     IOLoop.current().start()
#
# if __name__ == '__main__':
#     main()