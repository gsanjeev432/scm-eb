from django.contrib import admin

from .models import RawMaterial, Supplier


class RawMaterialInline(admin.TabularInline):
    model = RawMaterial
    extra = 1  # Number of empty forms to display

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company_name', 'location')
    search_fields = ('name', 'company_name', 'email')
    inlines = [RawMaterialInline]

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(RawMaterial)
