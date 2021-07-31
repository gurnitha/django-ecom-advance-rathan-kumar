## BUILDING ADVANCE DJANGO ECOMMERCE

github sourcecodes:
https://github.com/dev-rathankumar/greatkart-course
udemy:
https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/learn/lecture/25940412#questions/14475060


### ----------
### 1. SETUP
### ----------


#### 1.1 Initial commit

        new file:   .gitignore
        new file:   README.md


#### 1.2 Install django

        λ python -m venv venv3932
        λ venv3932\scripts\activate
        (venv3932) λ python -m pip install django
        (venv3932) λ python.exe -m pip install --upgrade pip


### ----------------------------
### 2. DJANGO PROJECT AND APPS
### ----------------------------


#### 2.1 Create django project 'src/config'

        (venv3932) λ django-admin startproject config .


#### 2.2 Create django app 'apps/main'


#### 2.3 Register the app 'main' to the project config/settings.py

        modified:   README.md
        modified:   apps/main/apps.py
        modified:   config/settings.py
        new file:   db.sqlite3


### -------------------------------
### 3. TEMPLATES AND STATIC FILES
### -------------------------------


#### 3.1 Hello world (Templates, Views, Urls)

        modified:   README.md
        new file:   apps/main/urls.py
        modified:   apps/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/main/index.html


#### 3.2 Adding html template and static assets for the home page

        modified:   README.md
        ...
        new file:   config/static/js/jquery-2.0.0.min.js
        new file:   config/static/js/script.js
        modified:   templates/main/index.html


#### 3.3 Creating STATIC_URL, STATIC_ROOT, STATICFILES_DIRS

        modified:   README.md
        modified:   config/settings.py


#### 3.4 Collect static files

        (venv3932) λ python manage.py collectstatic

        201 static files copied to 'E:\workspace\django\ECOMMERCE\rathan_advance_ecommerce\src\static'.

        modified:   README.md
        new file:   static/admin/fonts/Roboto-Bold-webfont.woff
        ...
        new file:   static/js/jquery-2.0.0.min.js
        new file:   static/js/script.js       


#### 3.5 Loading static files

        modified:   README.md
        modified:   templates/main/index.html


#### 3.6 Sagmenting the home page template

        modified:   README.md
        new file:   templates/main/inc/banner.html
        new file:   templates/main/inc/content.html
        modified:   templates/main/index.html
        new file:   templates/shared/footer.html
        new file:   templates/shared/head.html
        new file:   templates/shared/header-main.html
        new file:   templates/shared/header-top.html


#### 3.7 Base template

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/main/index.html


### -------------
### 3. DATABASE
### -------------


#### 3.1 Create .env file

        modified:   README.md
        new file:   config/.env


#### 3.2 Install django_environ 

        (venv3932) λ pip install django-environ


#### 3.3 Setting up .env file

        modified:   README.md
        modified:   config/.env


#### 3.4 Create database

        hp=# create database django_rathan_greatkart;
        CREATE DATABASE
        hp=# 

#### 3.5 Install database driver

        (venv3932) λ python -m pip install psycopg2-binary==2.8.6


#### 3.6 Adding db credentials and secret_key to .env file

        modified:   README.md
        modified:   config/.env


#### 3.7 Connecting .env file with the project settings.py

        modified:   README.md
        modified:   config/settings.py


### ------------------------
### 4. USER AUTHENTICATION
### ------------------------


#### 4.1 Create a new app 'apps/accounts'

        (venv3932) λ mkdir apps\accounts
        (venv3932) λ python manage.py startapp accounts apps/accounts


#### 4.2 Register accounts app to config/settings.py

        modified:   README.md
        modified:   apps/accounts/apps.py
        modified:   config/settings.py


#### 4.3 Creating Custom User using the AbstractBaseUser, BaseUserManager 

        modified:   README.md
        modified:   apps/accounts/admin.py
        new file:   apps/accounts/migrations/0001_initial.py
        modified:   apps/accounts/models.py
        modified:   config/settings.py


### --------------
### 5. CATEGORY
### --------------


#### 5.1 Create a new app 'apps/category'

        (venv3932) λ mkdir apps\category
        (venv3932) λ python manage.py startapp category apps/category


#### 5.2 Register the new app 'category' to config/settings.py

        modified:   README.md
        modified:   apps/category/apps.py
        modified:   config/settings.py


#### 5.3 Category model

        modified:   README.md
        modified:   apps/category/admin.py
        new file:   apps/category/migrations/0001_initial.py
        modified:   apps/category/models.py


#### 5.4 Pre-populated slug field based on category_name

        modified:   README.md
        modified:   apps/category/admin.py


#### 5.5 Add category items

        modified:   README.md
        new file:   photos/categories/01.png
        new file:   photos/categories/1.jpg
        new file:   photos/categories/12.jpg
        new file:   photos/categories/1_UEJo3RJ.jpg
        new file:   photos/categories/2.jpg
        new file:   photos/categories/3.jpg

        NOTE: 
        Could not access the image due to the media path        


#### 5.5 Add media path for category images

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   media/photos/categories/01.png
        new file:   media/photos/categories/1.jpg
        new file:   media/photos/categories/12.jpg
        new file:   media/photos/categories/2.jpg
        new file:   media/photos/categories/3.jpg

        NOTE: 
        1. To make images accessabel, re-insert the images
        2. A media folder created automatically in the project root    


### -----------
### 6. STORE
### -----------


#### 6.1 Create a new app 'apps/store'

        (venv3932) λ mkdir apps\store
        (venv3932) λ python manage.py startapp store apps/store


#### 6.2 Register the new app 'store' to config/settings.py

        modified:   README.md
        modified:   apps/store/apps.py
        modified:   config/settings.py


#### 6.3 Product model

        modified:   README.md
        modified:   apps/store/admin.py
        new file:   apps/store/migrations/0001_initial.py
        modified:   apps/store/models.py


#### 6.4 Modified product price field type form integer to decimal

        modified:   README.md
        modified:   apps/store/models.py


#### 6.5 Add items to product

        modified:   README.md
        new file:   media/photos/products/ATX-Jeans.jpg
        new file:   media/photos/products/Blue-Shirt.jpg
        new file:   media/photos/products/Great-Tshirt.jpg
        new file:   media/photos/products/Mavi_jeans.jpg
        new file:   media/photos/products/Puma-Ferrari-Shoes.jpg
        new file:   media/photos/products/US-Polo-Assn_Jacket.jpg
        new file:   media/photos/products/Wrangler-Shirt.jpg
        new file:   media/photos/products/jordan-true-flight-basketball-shoes.jpg


#### 6.6 Retrieve and display product items to home page

        modified:   README.md
        modified:   apps/main/views.py
        modified:   templates/main/inc/content.html


#### 6.7 Adding store-page (product-list) (VT Urls)

        modified:   README.md
        new file:   apps/store/urls.py
        modified:   apps/store/views.py
        modified:   config/urls.py
        new file:   templates/shared/breadcrumb.html
        modified:   templates/shared/header-main.html
        new file:   templates/store/inc/aside.html
        new file:   templates/store/inc/main-content.html
        new file:   templates/store/inc/pagination.html
        new file:   templates/store/store-page.html


#### 6.8 Retrieve and display product items to store-page

        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/inc/main-content.html

        NOTE:
        1. The template showing discount price.
        2. But in the model there is not discount price
        NEXT> Add discount price field in the product model


#### 6.9 Adding discount price field

        modified:   README.md
        modified:   apps/store/models.py
        modified:   templates/store/inc/main-content.html


#### 6.10 Product count

        modified:   README.md
        modified:   apps/store/views.py
        modified:   templates/store/inc/main-content.html

        # Views: Counting the products
        product_count = products.count()
        # Template
        <span class="mr-md-auto">Found <b>{{product_count}}</b> items </span>


#### 6.11 Retrieve all products_by_category

        http://127.0.0.1:8000/store/shirts

        path('<slug:category_slug>/', store_page, name='products_by_category'),

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

        modified:   README.md
        modified:   apps/store/urls.py
        modified:   apps/store/views.py


#### 6.12 CONTEXT_PROCESSOR - Part 1: create template 

        modified:   README.md
        new file:   apps/category/context_processors.py


#### 6.13 CONTEXT_PROCESSOR - Part 2: register it to TEMPLATES settings.py 

        modified:   README.md
        modified:   config/settings.py


#### 6.14 CONTEXT_PROCESSOR - Part 3: retrieve and display all categories in main menu

        modified:   README.md
        modified:   templates/shared/header-main.html


#### 6.15 CONTEXT_PROCESSOR - Part 4: create get_absolute_urls 

        modified:   README.md
        modified:   apps/category/models.py
        modified:   apps/store/urls.py


#### 6.16 CONTEXT_PROCESSOR - Part 5: use get_absolute_urls to links products_by_category

        modified:   README.md
        modified:   templates/shared/header-main.html


#### 6.17 No product found with that category

        modified:   README.md
        modified:   templates/store/inc/main-content.html


#### 6.18 Retrieve and display categories in aside menu of the store page (see 6.14) and add links (see 6.16)

        modified:   README.md
        modified:   templates/store/inc/aside.html


#### 6.19 Add All products to menus (aside and main manu)

        modified:   README.md
        modified:   templates/shared/header-main.html
        modified:   templates/store/inc/aside.html


#### 6.20 Creating product-detail template define the url

        NOTE:
        It works with this path:http://127.0.0.1:8000/store/anything/anything/

        modified:   README.md
        modified:   apps/store/urls.py
        modified:   apps/store/views.py
        new file:   templates/store/detail-page.html
        modified:   templates/store/inc/main-content.html


#### 6.21 Retrieve data and display it on product-detail page

        modified:   README.md
        modified:   apps/store/__pycache__/views.cpython-39.pyc
        modified:   apps/store/views.py
        modified:   templates/store/detail-page.html


#### 6.22 Create get_absolute_url function in Product model and use it to link product_detail

        modified:   README.md
        modified:   apps/store/models.py
        modified:   templates/main/inc/content.html
        modified:   templates/store/inc/main-content.html


#### 6.23 Linking all links

        modified:   README.md
        modified:   templates/main/inc/content.html
        modified:   templates/shared/header-main.html


#### 6.24 House keeping: re-naming of the path name to be consistent

        modified:   README.md
        modified:   apps/main/urls.py
        modified:   apps/store/urls.py
        modified:   templates/main/inc/content.html
        modified:   templates/shared/header-main.html
        modified:   templates/store/detail-page.html
        modified:   templates/store/inc/aside.html
        modified:   templates/store/inc/main-content.html


#### 6.25 Changing the banner

        modified:   README.md
        new file:   config/static/images/banners/cover.jpg
        new file:   static/images/banners/cover.jpg
        modified:   templates/main/inc/banner.html


#### 6.26 Loading the all.min.css

        modified:   README.md
        modified:   templates/shared/head.html
        modified:   templates/store/detail-page.html


#### 6.27 Showing No stock

        modified:   README.md
        modified:   templates/store/detail-page.html














































































































