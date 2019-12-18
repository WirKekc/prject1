from flask import Flask, request
import json, os
from flask_wtf import FlaskForm
from wtforms import StringField, validators


class ContactForm(FlaskForm):
    email = StringField(validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    password = StringField(validators=[
        validators.Length(min=6, max=35)
    ])
    confirm_pass = StringField(validators=[
        validators.Length(min=6, max=35)
    ])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/form/user', methods=['GET', 'POST'])
def post_valid():
    if request.method == 'POST':
        errors = []
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())
        if request.form['password'] != request.form['confirm_pass']:
            errors.append('Passwords not confirm')

        if form.validate():
            return (json.dumps({'status': 0, 'errors': errors}), 200)
        else:
            errors.append('Validation error')
            return (json.dumps({'status': 1, 'errors': errors}), 400)

    if request.method == 'GET':
        return 'hello world!', 200


@app.route('/locales')
def home():
    locales = json.dumps(['ru', 'en', 'it'])
    return locales


@app.route('/sum/<int:first>/<int:second>')
def summ(first, second):
    summ1 = first + second
    return str(summ1)


@app.route('/greet/<user_name>')
def greet(user_name):
    return 'Hello, ' + user_name


@app.route('/serve/<path:filename>')
def file(filename):
    a = ''
    if not os.path.exists('./files/'+filename):
        return '404: File doesnt exist'
    else:
        with open('./files/'+filename) as file:
            for line in file:
                a += line
            return a


if __name__ == '__main__':
    app.run()
