from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.utils.translation import gettext_lazy as _


class CustomAdminSite(admin.AdminSite):
    site_header = 'Supply Chain Management Admin'
    site_title = 'SCM Admin'
    index_title = 'Welcome to SCM Admin Panel'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        context = {
            'orders_count': Order.objects.count(),
            'suppliers_count': Supplier.objects.count(),
            'manufacturers_count': Manufacturer.objects.count(),
        }
        return render(request, 'admin/dashboard.html', context)

admin_site = CustomAdminSite(name='custom_admin')
admin_site.register(Supplier)
admin_site.register(Manufacturer)
admin_site.register(Customer)
admin_site.register(Order)
