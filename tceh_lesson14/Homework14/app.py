from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import tceh_lesson14.Homework14.config as config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/article', methods=['GET', 'POST'])
def article_index():
    from tceh_lesson14.Homework14.models import Article
    from tceh_lesson14.Homework14.forms import ArticleForm

    if request.method == 'POST':
        print(request.form)
        article_form = ArticleForm(request.form)

        if article_form.validate():
            article_note = Article(**article_form.data)
            db.session.add(article_note)
            db.session.commit()

            flash('Article create')
        else:
            flash('Article form not valid! Article was not create!')
            flash(str(article_form.errors))
    return render_template('articles.txt')


@app.route('/comment', methods=['GET', 'POST'])
def comments_index():
    from tceh_lesson14.Homework14.models import Post
    from tceh_lesson14.Homework14.forms import PostForm

    if request.method == 'POST':
        print(request.form)
        post_form = PostForm(request.form)

        if post_form.validate():
            post_note = Post(**post_form.data)
            db.session.add(post_note)
            db.session.commit()

            flash('Comment create')
        else:
            flash('Post form not valid! Comment was not create!')
            flash(str(post_form.errors))
            print(post_form.validate())
    return render_template('comments.txt')


@app.route('/')
def all_notes():
    article_notes = Article.query.all()
    article_text = article_notes[0].article_text
    for note in article_notes:
        print(article_text)
        print(note.article_text)

    post_notes = Post.query.all()
    post_text = post_notes[0].post_text
    for note in post_notes:
        print(post_text)
        print(note.post_text)
    return render_template('articles_and_comments.txt', article_notes=article_notes, post_notes=post_notes )


def first_note():
    print('First note!')
    user1 = Article(article_text='This is first note!')
    db.session.add(user1)
    db.session.commit()


if __name__ == '__main__':
    from tceh_lesson14.Homework14.models import *
    db.create_all()

    if Article.query.count() == 0:
        first_note()

    new_Article = Article.query.all()
    print(list(map(str, new_Article)))

    app.run()
