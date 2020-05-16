# -*- coding: utf-8 -*-
# Программа должна содержать:
# 1) модель GuessBookItem
# 1.1 поле автор: любое значение
# 1.2 Дата и время публикации
# 1.4 Булевое поле: удалено или нет


from datetime import date
from tceh_lesson13.Homework13.app import db


class GuessBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    note_in_book = db.Column(db.String(140), unique=False, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=False)
    date_create = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return f'< Author of note {self.note_in_book} is {self.author}>'
