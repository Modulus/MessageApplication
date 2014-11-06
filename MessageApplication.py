from flask import Flask

#app = Flask(__name__, static_folder='webapp/dist', static_url_path='')

app = Flask(__name__)

@app.route('/')
def serve_root():
    return 'Hello world!'



# @app.route('/')
# def serve_root():
#     return app.send_static_file('index.html')


# if __name__ == '__main__':
#     app.run()
