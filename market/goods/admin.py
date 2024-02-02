from django.contrib import admin
from goods.models import *

# Register your models here.

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):  # автоматическое заполнение поля 'slug' по названию поля 'name'
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):  # автоматическое заполнение поля 'slug' по названию поля 'name'
    prepopulated_fields = {
        'slug': ('name',)
    }
