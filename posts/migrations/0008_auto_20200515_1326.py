# Generated by Django 2.1 on 2020-05-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200514_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('law_politics', '法学・政治学'), ('medical', '医学・薬学'), ('engineering', '工学'), ('social', '人文社会'), ('science', '理学'), ('agriculture', '農学'), ('economics', '経済学'), ('liberal_arts', '教養'), ('education', '教育学')], default='', max_length=10, unique=True, verbose_name='カテゴリー選択'),
        ),
    ]
