# Generated by Django 3.2.5 on 2021-07-22 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_bookmarks_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarks',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_news', to='main.news', verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='bookmarks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
