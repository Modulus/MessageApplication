from tornado.web import RequestHandler, Application, FallbackHandler, os, StaticFileHandler

__author__ = 'johska'

from MessageApplication import app

from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.httpserver import  HTTPServer

class MainHandler(RequestHandler):
    def get(self):
        self.render('webapp/dist/index.html')

settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'webapp', 'dist'),
    'templates_path': os.path.join(os.path.dirname(__file__), 'webapp', 'dist')

}


container = WSGIContainer(app)
application = Application([
    (r'/', MainHandler),
    (r'.*', StaticFileHandler, dict(path=settings['static_path']))], **settings)


if __name__ == '__main__':
    application.listen(5000)
    IOLoop.instance().start()

#
# http_server = HTTPServer(WSGIContainer(app))
# http_server.listen(5000)
# IOLoop.instance().start()

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