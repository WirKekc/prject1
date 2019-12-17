from flask import Flask
import json


app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
