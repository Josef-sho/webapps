from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError, input_required, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some_secret_string"

class Form(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message=None)])
    submit = SubmitField(label='Login')


# class LoginForm(FlaskForm):
#     email = EmailField(label='Email', validators=[DataRequired(), Email()])
#     password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message=None)])
#     submit = SubmitField(label='Login')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", 'post'])
def login():
    form = Form()
    form.validate_on_submit()
    print(form.email.data)
    return render_template("login.html", form=form)


@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)