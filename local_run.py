from flask import Flask

from app.blueprints import user_api
from app.blueprints import message_api

__author__ = 'johska'


app = Flask(__name__, static_folder='webapp/dist', static_url_path='')
app.config.from_object('config.ProdConfig')

app.register_blueprint(user_api, url_prefix="/api/user")
app.register_blueprint(message_api, url_prefix="/api/message")


@app.route('/')
def serve_root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 5000, app, use_reloader=True)
