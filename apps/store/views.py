# apps/store/views.py

# Django modules
from django.shortcuts import render, get_object_or_404

# Django locals
from apps.store.models import Product
from apps.category.models import Category

# Create your views here.

# # Store_page view 1
# def store_page(request):

# 	# Get all the available products
# 	products = Product.objects.all().filter(is_available=True)

# 	# Counting the products
# 	product_count = products.count()

# 	# Put the available products into context dictionary
# 	context = {
# 		'products':products, # <-- 'products'  as variable
# 		'product_count':product_count,
# 	}	

# 	return render(request, 'store/store-page.html', context)


# Store_page view 2 + slug
def store_page(request,category_slug=None):

	# Define categories and products are None
	categories = None
	products   = None

	# What if categories slug are NOT None or exist
	# Return the slugs if they are exist, or
	# return 404 error if they are not exist
	if category_slug != None:
		categories = get_object_or_404(Category, slug=category_slug)
		products   = Product.objects.filter(category=categories, is_available=True)

		# Product count
		product_count = products.count()

	else:

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



def detail_page(request,category_slug,product_slug):
	return render(request, 'store/detail-page.html')