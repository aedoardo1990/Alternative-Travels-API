from django.contrib import admin
from .models import Marketplace

@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'created_at',
        'updated_at',
        'title',
        'status',
        'condition',
        'details',
        'image',
        'address',
        'contact_number',
        'email', 
        'price_with_EUR'
        ]