from typing import Tuple
from django.db import models
from django.utils import timezone

class Post(models.Model):
    # 定义一个模型 这是一个对象
        # class 关键字 定义对象
        # Post 模型的名字，总是大写开头作为类名
        # models.Model Post是一个Django模型
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # models.ForeignKey 指向另一个模型的链接
    title = models.CharField(max_length=200)
    # models.CharField 用长度有限制的字符串来定义一个文本
    text = models.TextField()
    # models.TextField 无长度限制的长文本
    created_date = models.DateTimeField(default=timezone.now)
    # models.DateTime 日期和时间
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title