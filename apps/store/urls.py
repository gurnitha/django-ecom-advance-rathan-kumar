# apps/store/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.store.views import store_page, detail_page

# App name
app_name = 'store'

urlpatterns = [
    path('', store_page, name='store-page'),
    path('<slug:category_slug>/', store_page, name='product_list_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', detail_page, name='product_detail'),
]
