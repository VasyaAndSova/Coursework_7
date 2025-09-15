from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "is_published")
    list_filter = ("category", "is_published")
    search_fields = ("name", "description")


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
