from flask import Flask, render_template
from datetime import datetime
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/<string:name>')

@app.route('/<name>')
def greeting(name):
    year = datetime.today().year
    gender = requests.get(f"https://api.genderize.io?name={name}").json()['gender']
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    return render_template("index.html", year=year, name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)