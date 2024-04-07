from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'post',
        'created_at'
        ]
