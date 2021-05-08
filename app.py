from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Hello world welcome to python flask app</h2>'

if __name__ == '__main__':
    app.run(threaded=True)