from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PostMessage(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_massage')
    post_title = models.CharField(null=False, blank=False, verbose_name='Заноловок статьи', max_length=20)
    post_text = models.CharField(null=False, blank=False, verbose_name='Текст поста: ', max_length=255)
    post_likes = models.IntegerField(default=0, verbose_name='Понравилось: ')
    post_date = models.DateTimeField(null=False, blank=False, default=datetime.now())

    def __str__(self):
        return self.post_title

    def foreignkey_user(self, db_field, request, **kwargs):
        if db_field.name == 'post_user':
            kwargs['initial'] = request.user.id
        return super(PostMessage, self).foreignkey_user(
            db_field, request, **kwargs
        )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Список постов'
        # ordering = ['post_date', 'post_likes', 'post_title']


class Comment(models.Model):
    comment_text = models.CharField(null=True, blank=True, verbose_name='Комметарий', max_length=255)
    comment_post = models.ForeignKey(PostMessage, null=False)
    comment_date = models.DateTimeField(null=False, blank=False, default=datetime.now())
    comment_user = models.ForeignKey(User, related_name='comment_massage')

    class Meta:
        verbose_name = 'Комметарий'
        verbose_name_plural = 'Комметарии'
        ordering = ['comment_date']

    def __str__(self):
        return self.comment_text