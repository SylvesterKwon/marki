from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    recent_edit_date = models.DateTimeField()

    def __str__(self):
        return self.title

    # 해당 article 조회 url 리턴하는 method?


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    create_date = models.DateTimeField()