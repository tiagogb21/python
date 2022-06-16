from flask import Flask
from random import randint

app = Flask(__name__)

aleatory = randint(0, 10)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="aleatory numbers" />'


@app.route('/<int:guss_number>')
def show_post(guss_number):
    # show the post with the given id, the id is an integer
    if(guss_number < aleatory):
        return '<p> it\'s too low </p><br/>' \
            '<img src="https://media4.giphy.com/media/UohTsyhfrsPFm/giphy.gif?cid=ecf05e47mookkg04aimpbv6oyfs3skb223pnk7ni6ve2llmh&rid=giphy.gif&ct=g" alt="sad dog"/>'
    if(guss_number > aleatory):
        return '<p> it\'s too high </p><br/>' \
            '<img src="https://media1.giphy.com/media/W9gHkIonu8qXI7AC1y/giphy.webp?cid=ecf05e47mookkg04aimpbv6oyfs3skb223pnk7ni6ve2llmh&rid=giphy.webp&ct=g" alt="sad dog">'
    if(guss_number == aleatory):
        return '<p> You found me! </p><br/>' \
            '<img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="happy bear">'


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
