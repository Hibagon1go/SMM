# Generated by Django 2.1 on 2020-05-09 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_like_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
    ]
