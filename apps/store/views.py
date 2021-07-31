# apps/store/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.store.models import Product

# Create your views here.
def store_page(request):

	# Get all the available products
	products = Product.objects.all().filter(is_available=True)

	# Put the available products into context dictionary
	context = {
		'products':products # <-- 'products'  as variable
	}	

	return render(request, 'store/store-page.html', context)


