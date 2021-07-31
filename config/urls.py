# config/urls.py

# Django modules
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    # Main app
    path('', include('apps.main.urls', namespace='main')),
    # Store app
    path('store/', include('apps.store.urls', namespace='store')),
    # Cart app
    path('cart/', include('apps.cart.urls', namespace='cart'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
