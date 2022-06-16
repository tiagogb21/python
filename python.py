from flask import Flask

app = Flask(__name__)


@app.route('/')
def bye():
    return "Hello!"


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run()
