from datetime import date
from tceh_lesson14.Homework14.app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_text = db.Column(db.String(2000), unique=False, nullable=False)
    date_create = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(
        db.Integer,
        db.ForeignKey('article.id'),
        default=0,
        nullable=False,
        index=True
    )
    article = db.relationship(Article, foreign_keys=[article_id, ])

    post_text = db.Column(db.String(200), unique=False, nullable=False)
    date_create = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)




