# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>Hello!<h1>"


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
