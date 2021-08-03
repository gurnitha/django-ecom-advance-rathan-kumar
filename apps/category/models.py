# apps/category/models.py

# Django modules
from django.db import models
from django.urls import reverse
from django.apps import apps

# Django locals

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])
            
    def __str__(self):
        return self.category_name


    def get_pr_count(self):
        Product = apps.get_model('store', 'Product')
        products = Product.objects.filter(category=self)
        count = products.count()
        return count
