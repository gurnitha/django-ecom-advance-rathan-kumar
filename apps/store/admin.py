# apps/store/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.store.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug',
    				'price', 'stock', 
    				'category', 
    				'modified_date', 
    				'is_available')
    prepopulated_fields = {'slug': ('product_name',)}