# Generated by Django 3.2.5 on 2021-07-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bookmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarks',
            name='book',
            field=models.BooleanField(default=False),
        ),
    ]