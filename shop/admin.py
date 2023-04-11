from django.contrib import admin
from .models import Products, Order

admin.site.site_header = 'E-commerce admin pannel'
admin.site.site_title = 'E-commerce site'
admin.site.index_title = 'E-commerce administration'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'description', 'image')
    search_fields = ('title', 'category')
    actions = ('change_category_to_default',)
    
    def change_category_to_default(self,request, queryset):
        queryset.update(category='default')


admin.site.register(Products, ProductAdmin)
admin.site.register(Order)