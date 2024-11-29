from django.contrib import admin

from .models import Manufacturer, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1  # Number of empty forms to display

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company_name', 'location')
    search_fields = ('name', 'company_name', 'email')
    inlines = [ProductInline]
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price', 'stock', 'approved')
    list_filter = ('approved',)
    actions = ['approve_products', 'reject_products']

    def approve_products(self, request, queryset):
        queryset.update(approved=True)
    approve_products.short_description = "Approve selected products"

    def reject_products(self, request, queryset):
        queryset.update(approved=False)
    reject_products.short_description = "Reject selected products"

admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
