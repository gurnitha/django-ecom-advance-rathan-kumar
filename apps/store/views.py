# apps/store/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.store.models import Product

# Create your views here.
def store_page(request):

	# Get all the available products
	products = Product.objects.all().filter(is_available=True)

	# Counting the products
	product_count = products.count()

	# Put the available products into context dictionary
	context = {
		'products':products, # <-- 'products'  as variable
		'product_count':product_count,
	}	

	return render(request, 'store/store-page.html', context)


