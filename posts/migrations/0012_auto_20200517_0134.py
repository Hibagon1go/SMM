# Generated by Django 2.1 on 2020-05-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200515_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='agriculture',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='economics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='education',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='engineering',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='law_politics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='liberal_arts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='medical',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='nongenre',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='science',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='society',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
