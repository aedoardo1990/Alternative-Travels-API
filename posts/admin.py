from django.contrib import admin
from .models import Post
import tagulous.admin


admin.site.register(Post)
tagulous.admin.register(Post.tags)
