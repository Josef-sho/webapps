from flask import Flask, render_template
from datetime import datetime
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")




@app.route('/<name>')
def greeting(name):
    year = datetime.today().year
    gender = requests.get(f"https://api.genderize.io?name={name}").json()['gender']
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    return render_template("index.html", year=year, name=name, gender=gender, age=age)


@app.route('/blog')
def blog():
    all_post = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=all_post, greeting=greeting)

if __name__ == "__main__":
    app.run(debug=True)
