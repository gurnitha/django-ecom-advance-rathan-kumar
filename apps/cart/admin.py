# apps/cart/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.cart.models import Cart, CartItem

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)