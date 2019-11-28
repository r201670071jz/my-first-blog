from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)#管理者ページに作成したモデルが編集できるようにする。引数はクラス名