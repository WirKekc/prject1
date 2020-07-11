from wtforms_alchemy import ModelForm

from tceh_lesson14.Homework14.models import Article, Post


class ArticleForm(ModelForm):
    class Meta:
        model = Article


class PostForm(ModelForm):
    class Meta:
        model = Post
