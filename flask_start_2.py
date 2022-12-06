from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!<h1>' \
           '<img src="https://giphy.com/stories/nfl-sunday-gifs-you-missed-7ce4fec7-318c" width = 200>'

'''@app.route('/<name>')
def greeting(name):
    return 'hello ' + name
'''
@app.route('/<path:hello>')
def check(hello):
    return "hi"

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper



@make_bold
@app.route('/bye')
def bye():
    return 'hello from the other side'


app.run(debug=True)