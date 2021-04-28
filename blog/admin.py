from django.contrib import admin
from .models import Post

#  导入并注册模型
admin.site.register(Post)