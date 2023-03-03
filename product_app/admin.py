from django.contrib import admin

from product_app.models import Category, Manufacturer, Product

admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Product)
