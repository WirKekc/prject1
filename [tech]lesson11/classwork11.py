from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, validators


class ContactForm(FlaskForm):
    number = StringField(validators=[
        validators.Length(min=1, max=10)
    ])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This is secret',
    WTF_CSRF_ENABLES=False
)


@app.route('/')
def home():
    return 'Hello word!!'


if __name__ == '__main__':
    app.run()
