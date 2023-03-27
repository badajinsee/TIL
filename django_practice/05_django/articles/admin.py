from django.contrib import admin
from .models import Article

# Register your models here.
# 암기 꿀팁 : admin site 에 등록(register) 하겠다.
admin.site.register(Article)