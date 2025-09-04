from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_featured', 'stock', 'brand', 'rating')
    list_filter = ('category', 'is_featured', 'brand')
    search_fields = ('name', 'description', 'brand')
