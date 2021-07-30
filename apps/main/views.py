# apps/main/views.py

# Django modules
from django.shortcuts import render

# Django locals

# Create your views here.
def home_page(request):
	return render(request, 'main/index.html')