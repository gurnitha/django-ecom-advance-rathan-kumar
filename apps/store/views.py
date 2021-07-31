# apps/store/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.store.models import Product

# Create your views here.
def store_page(request):
	return render(request, 'store/store-page.html')