from flask import Flask
import random

app = Flask(__name__)
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
choice = random.choice(li)


@app.route('/')
def run():
    return "<h1>Guess a number between 0 and 9<h1>" \
           "<img src='https://media.giphy.com/media/dudpGUNsMDXeovGSAV/giphy.gif' >"

@app.route("/<int:name>")
def greeting(name):
    if name < choice:
        return "<h1> sorry thats too low" \
               "<img src='https://media.giphy.com/media/dudpGUNsMDXeovGSAV/giphy.gif' >"
    elif name > choice:
        return "<h1> sorry thats too high" \
               "<img src='https://media.giphy.com/media/ntwtrcosVg0zS6mruP/giphy.gif' >"

    else :
        return "<h1> thats just right<h1>" \
               "<img src= 'https://media.giphy.com/media/DyQrKMpqkAhNHZ1iWe/giphy.gif >'"


app.run(debug=True)