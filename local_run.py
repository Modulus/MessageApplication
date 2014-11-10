from flask import Flask

__author__ = 'johska'


app = Flask(__name__, static_folder='webapp/dist', static_url_path='')


@app.route('/')
def serve_root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()