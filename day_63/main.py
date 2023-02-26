from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-book-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    review = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()
    books = Book.query.all()

@app.route('/')
def home():
    return render_template('index.html', dict = books)


@app.route("/add", methods =['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']

        with app.app_context():
            new_book = Book( title=f"{title}", author=f"{author}", review=f"{rating}")
            db.session.add(new_book)
            db.session.commit()
        return redirect('/')
    else:
        return render_template('add.html', dict = books)



if __name__ == "__main__":
    app.run(debug=True)

