# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route('/user/<username>')
def welcome():
    return 'User %s' % escape(username)


if __name__ == "__main__":
    app.run()
