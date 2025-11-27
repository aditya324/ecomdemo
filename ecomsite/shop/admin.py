from django.contrib import admin
from .models import Products, Order

# Register your models here.

admin.site.site_header="Ecom Admin"
admin.site.index_title="Abc shopping"
admin.site.site_title="Abc shopping"


class OrderAdmin(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'city', 'state', 'zipcode', 'total')
    search_fields = ('name', 'email', 'address', 'city', 'state', 'zipcode', 'total')
class ProductsAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')
    
    change_category_to_default.short_description = "Change category to default"
    list_display = ('title', 'price', 'discounted_price', 'category', 'description', 'image')
    search_fields = ('title', 'price', 'discounted_price', 'category', 'description', 'image')
    actions = [change_category_to_default]
    fields=('title', 'price', 'discounted_price', 'category', 'description', 'image')
    list_editable = ('price', 'discounted_price', 'category', 'description', 'image')
   



admin.site.register(Order, OrderAdmin)
admin.site.register(Products, ProductsAdmin)
