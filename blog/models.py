from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class PostMessage(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_massage', verbose_name='Автор')
    title = models.CharField(null=False, blank=False, verbose_name='Заголовок статьи', max_length=20)
    text = models.CharField(null=False, blank=False, verbose_name='Текст поста', max_length=255)
    likes = models.IntegerField(default=0, verbose_name='Понравилось')
    date = models.DateTimeField(null=False, blank=False, default=datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Список постов'
        ordering = ['date', 'likes', 'title']


class Comment(models.Model):
    text = models.CharField(null=True, blank=True, verbose_name='Комметарий', max_length=255)
    post = models.ForeignKey(PostMessage, null=False)
    date = models.DateTimeField(null=False, blank=False, default=datetime.now())
    user = models.ForeignKey(User, related_name='comment_massage')

    class Meta:
        verbose_name = 'Комметарий'
        verbose_name_plural = 'Комметарии'
        ordering = ['date']

    def __str__(self):
        return self.text