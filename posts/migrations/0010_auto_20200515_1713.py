# Generated by Django 2.1 on 2020-05-15 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200515_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='timestamp',
        ),
    ]
