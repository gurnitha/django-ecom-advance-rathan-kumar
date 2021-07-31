# apps/store/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.store.views import store_page

# App name
app_name = 'store'

urlpatterns = [
    path('', store_page, name='store-page'),
]
