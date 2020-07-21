from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import tceh_lesson14.Homework14.config as config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/comments_only', methods=['GET', 'POST'])
def comments_only():
    post_notes = Post.query.all()
    # post_text = post_notes[0].post_text
    for note in post_notes:
        # print(post_text)
        print(note.post_text)
    return render_template('comments_only.txt', post_notes=post_notes)


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
            post_data = Post.query.all()
            post_text = post_data[-1].post_text
            flash(post_text)
        else:
            flash('Post form not valid! Comment was not create!')
            flash(str(post_form.errors))
            print(post_form.validate())
    return render_template('comments.txt')


@app.route('/')
def all_notes():
    article_notes = Article.query.all()
    # article_text = article_notes[0].article_text
    for note in article_notes:
        # print(article_text)
        print(note.article_text)

    post_notes = Post.query.all()
    # post_text = post_notes[0].post_text
    for note in post_notes:
        # print(post_text)
        print(note.post_text)
    return render_template('articles_and_comments.txt', article_notes=article_notes, post_notes=post_notes)


def first_note():
    print('First note!')
    user1 = Article(article_text='''
    Правильное питание - это система приема пищи, которая обеспечивает рост, жизнедеятельность, и здоровье нашего организма.
    Правильное питание включает в себя содержание всех полезных веществ, которые дарят нам энергию и бодрость, а это залог нашего здоровья.
    Если вы хотите следовать правильному питанию, то необходимо контролировать принятие в пищу жиров, белков, и углеводов.
    Нужно отдавать предпочтение нежирным сортам мяса и овощам.
    Следует отказаться от фастфуда, большого количества сладостей, алкоголя, курения, и других вредных привычек.
    Нужно соблюдать режим приема пищи, и стараться кушать каждый день в одно и то же время.
    Не переедать, и не оставаться голодным.
    ''')
    comment1 = Post(post_text='This is first comment!', article_id=0)
    db.session.add(user1)
    db.session.add(comment1)
    db.session.commit()


if __name__ == '__main__':
    from tceh_lesson14.Homework14.models import *
    db.create_all()

    # Очищение табицы
    # Article.query.delete()
    # Post.query.delete()

    # Проверка. Если на странице ничего нет, то добавляем статью и первый коментарий.
    if Article.query.count() == 0 and Post.query.count() == 0:
        first_note()

    new_Post = Post.query.all()
    print(list(map(str, new_Post)))

    new_Article = Article.query.all()
    print(list(map(str, new_Article)))

    app.run()
