# Generated by Django 3.2.5 on 2021-07-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_confirmationcode_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationcode',
            name='code',
            field=models.CharField(max_length=100),
        ),
    ]