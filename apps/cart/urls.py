# apps/cart/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.cart.views import cart_page

# App name
app_name = 'cart'

urlpatterns = [
    path('', cart_page, name='cart_page'),
]
