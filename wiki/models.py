from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    parent_article = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    summary = models.CharField(max_length=200)
    content = models.TextField(max_length=100000)
    create_date = models.DateTimeField()
    recent_edit_date = models.DateTimeField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # 해당 article 조회 url 리턴하는 method?


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=1000)
    create_date = models.DateTimeField()