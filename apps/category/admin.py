# apps/category/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.category.models import Category

# Register your models here.
admin.site.register(Category)