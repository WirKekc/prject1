from wtforms_alchemy import ModelForm

from tceh_lesson15.Homework15.models import Article, Post


class ArticleForm(ModelForm):
    class Meta:
        model = Article


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = [
            'article_id',
        ]
