from flask import Flask
import os


app = Flask(__name__)


@app.route('/hello/<user>')
def home(user):
    return 'Hello user: ' + user


@app.route('/conc/<int:a>+<int:b>')
def conc(a, b):
    c = a + b
    return 'a + b = ' + str(c)


@app.route('/length/<a>,<b>,<c>')
def length(a, b, c):
    if len(a) > len(b):
        if len(a) > len(c):
            return a
        else:
            return c
    else:
        if len(b) > len(c):
            return b
        else:
            return c


@app.route('/filepath/<path:a>')
def file(a):
    if a == os.getcwd()[1:]:
        return 'Да'
    else:
        return'Нет'


if __name__ == '__main__':
    app.run()



