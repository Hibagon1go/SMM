from django.db import models

from accounts.models import User #changed


Genre_Choices = (
    ('law_politics', '法学・政治学'),
    ('medical', '医学・薬学'),
    ('engineering', '工学'),
    ('social', '人文社会'),
    ('science', '理学'),
    ('agriculture', '農学'),
    ('economics', '経済学'),
    ('liberal_arts', '教養'),
    ('education', '教育学'),
) #分野の選択肢 added
    


class Post(models.Model):
    author = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to="image/posts/", blank=True, null=True)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class Like(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    
class Comment(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    text = models.TextField(blank=True)

