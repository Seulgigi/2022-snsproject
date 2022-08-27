from django.contrib import admin
from .models import Post, LifePost

# Register your models here.
admin.site.register(Post)
admin.site.register(LifePost)