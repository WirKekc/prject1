# -*- coding: utf-8 -*-

# from flask_wtf import FlaskForm
# from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from tceh_lesson13.Homework13.models import GuessBookItem

class GuessBookForm(ModelForm):
    class Meta:
        model = GuessBookItem

