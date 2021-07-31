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
































































































































































































