from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

# Field = 画面上でユーザーが入力する場所
class Comment(models.Model):
# ForeignKey = 記事とコメントを結びつける言葉
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments')
# CharField = 文字列（２００文字が最大の文字列）
    author = models.CharField(max_length=200)
# TextField = 長い文字列
    text = models.TextField()
# DateTimeField = 日付のこと
    created_date = models.DateTimeField(default=timezone.now)
# BooleanField = コメントの許可する場所
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def __str__(self):
        return self.text

    # def approved_comments(self):
        # return self.comments.filter(approved_comment=True)

# Create your models here.
