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





























































































































































































































































