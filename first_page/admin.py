from django.contrib import admin

from first_page.models import Product, Category, Shop

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Shop)
# Register your models here.
