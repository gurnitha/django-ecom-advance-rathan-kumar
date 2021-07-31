# apps/category/context_processors.py

# Django modules

# Django locals
from apps.category.models import Category

# The context processor takes a request 
# as an argument and 
# it will return the dictionary of data as a context.

def menu_links(request):

	# Get all the category objects
	links = Category.objects.all()
	print(links)
	# Put the available category object into context dictionary
	context = {
		'links':links, # <-- 'links'  as variable
	}

	return dict(context)	