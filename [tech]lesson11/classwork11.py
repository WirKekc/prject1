from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators
import random
# import os
#
# os.environ['S'] = 'something'
random.seed(1)
rand = random.randint(1, 50)


class ContactForm(FlaskForm):
    number = StringField(validators=[
        validators.Length(min=1, max=10)
    ])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This is secret',
    WTF_CSRF_ENABLES=False,
    FLASK_RANDOM_SEED=random.seed(1)
)

def rerand():
    global rand
    rand = random.randint(1, 50)

@app.route('/guess/', methods=['GET', 'POST'])
def guess1():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())
        if int(request.form['number']) > rand:
            return '>'
        if int(request.form['number']) < rand:
            return '<'
        if int(request.form['number']) == rand:
            rerand()
            return '='
        if form.validate():
            return 200
        else:
            return 'Что то не так!'
    if request.method == 'GET':
        return 'Сделайте POST запрос', 200


@app.route('/')
def home():
    return 'Число загадано!!'


if __name__ == '__main__':
    app.run()
