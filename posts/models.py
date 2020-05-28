from django.db import models
from django.db.models import Count, Q
from accounts.models import User #changed
from django.utils import timezone


#class Category(models.Model):
    #Category_Choices = (
      #('法学・政治学', 'law_politics'),
      #('医学・薬学', 'medical'),
      #('工学', 'engineering'),
      #('人文社会', 'social'),
      #('理学', 'science'),
      #('農学', 'agriculture'),
      #('経済学', 'economics'),
      #('教養', 'liberal_arts'),
      #('教育学', 'education' ),
      #('ノンジャンル', 'nongenre')
    #)

    #name = models.CharField(verbose_name="カテゴリー", max_length=10, choices=Category_Choices, unique=True, default='')
    #slug = models.SlugField(unique=True)
    #timestamp = models.DateTimeField(auto_now_add=True)
        

    #def __str__(self):
       # return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    #slug = models.SlugField(unique=True)
    #timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE)
    #category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField('タイトルを入力してください',max_length=255)
    
    text = models.TextField("本文", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField("公開",default=False)
    law_politics = models.BooleanField("法律/政治",default=False)
    medical = models.BooleanField("医療系",default=False)
    engineering = models.BooleanField("工学系",default=False)
    society = models.BooleanField("社会学系",default=False)
    science = models.BooleanField('理学系',default=False)
    agriculture = models.BooleanField("農学系",default=False)
    economics = models.BooleanField("経済",default=False)
    education = models.BooleanField("教育",default=False)
    liberal_arts = models.BooleanField("教養",default=False)
    nongenre = models.BooleanField("その他",default=False)

    class Meta:
        ordering = ['-created_at']


    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.title

class Like(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    
class Comment(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    text = models.TextField(blank=True)

