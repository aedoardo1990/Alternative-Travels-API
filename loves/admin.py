from django.contrib import admin
from .models import Love


@admin.register(Love)
class LoveAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'marketplace',
        'created_at'
        ]
