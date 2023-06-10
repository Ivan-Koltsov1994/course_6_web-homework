from django.contrib import admin

from catalog.models import Product, Category, Version


# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unit_price', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'number_version', 'title_version', 'is_active',)