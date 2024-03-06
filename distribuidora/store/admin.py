from django.contrib import admin
from .models import Category, Product, Customer, Order

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'sale']
    list_filter = ['category', 'sale']
    search_fields = ['name', 'description']
admin.site.register(Product, ProductAdmin)

admin.site.register(Customer)

admin.site.register(Order)

