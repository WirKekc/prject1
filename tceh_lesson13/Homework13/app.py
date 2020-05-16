# -*- coding: utf-8 -*-

# Программа должна содержать:
# 1) модель GuessBookItem
# 1.1 поле автор: любое значение
# 1.2 Дата и время публикации
# 1.4 Булевое поле: удалено или нет
#
# 2 Вы должны иметь возможность получить все запаси по адресу "/"
# 2 Вы должны иметь возможность добавить запись по адресу "/create"
# 3.1 Должна работать валидация при помощи формы модели...

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import tceh_lesson13.Homework13.config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/create', methods=['GET', 'POST'])
def index():
    from tceh_lesson13.Homework13.models import GuessBookItem
    from tceh_lesson13.Homework13.forms import GuessBookForm

    if request.method == 'POST':
        print(request.form)
        form = GuessBookForm(request.form)

        if form.validate():
            note = GuessBookItem(**form.data)
            db.session.add(note)
            db.session.commit()

            flash('Note create!')
        else:
            flash('Form is not valid! Note was not created')
            flash(str(form.errors))

    # notes = GuessBookItem.query.all()
    # author = notes[0].author
    # note_in_book = notes[0].note_in_book
    # for note in notes:
    #     print(author, note_in_book)
    #     print(note.author, note.note_in_book)
    #
    return render_template('home.txt')

@app.route('/')
def all_notes():
    notes = GuessBookItem.query.all()
    author = notes[0].author
    note_in_book = notes[0].note_in_book
    for note in notes:
        print(author, note_in_book)
        print(note.author, note.note_in_book)
    return render_template('all_notes.txt', notes=notes)


def populate_db():
    print('Creating First Note!')
    # Creating new ones
    ivan = GuessBookItem(author='Ivan', note_in_book='First note')

    db.session.add(ivan)
    db.session.commit()


if __name__ == '__main__':
    from tceh_lesson13.Homework13.models import *
    db.create_all()

    if GuessBookItem.query.count() == 0:
        populate_db()

    guessBooks = GuessBookItem.query.all()
    print(list(map(str, guessBooks)))

    #Running app:
    app.run()

