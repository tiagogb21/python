# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<strong>" + function() + "<strong>"


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "<em>"


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "<u>"


@app.route('/')
@make_bold
@make_emphasis
@make_underline
def hello():
    return '<h1 style="text-align: center"> Hello! </h1>' \
        '<p>Be happy!</p>' \
        '<img src="https://media1.giphy.com/media/tsX3YMWYzDPjAARfeg/giphy.gif?cid=ecf05e47a097543c99e9fee7d723e87883089bac3959d79f&rid=giphy.gif&ct=g" alt="dancing bear">'


@app.route('/user/<username>')
# Para usar o parâmetro da url,
# precisa passar um parâmetro para a função
def show_user_profile(username):
    return 'Welcome, %s' % escape(username)


# <converter:variable_name>
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
