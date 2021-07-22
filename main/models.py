from django.db import models

# Create your models here.
from rest_framework.authtoken.admin import User


def upload_to(instance, filename):
    return filename


class News(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField()


class ImageNews(models.Model):
    image = models.ImageField(upload_to=upload_to)
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class Bookmarks(models.Model):
    book = models.BooleanField(default=False)
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость', related_name="book_news")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name="bookmarks")
