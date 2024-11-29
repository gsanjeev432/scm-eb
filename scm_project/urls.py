"""
URL configuration for scm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suppliers/', include('supplier.urls')),
    path('manufacturers/', include('manufacturer.urls')),
    path('customers/', include('customer.urls')),
    path('orders/', include('orders.urls')),
    path('', lambda request: render(request, 'home.html'), name='home'),
    path('suppliers/', lambda request: render(request, 'suppliers.html'), name='suppliers'),
    path('manufacturers/', lambda request: render(request, 'manufacturers.html'), name='manufacturers'),
    path('customers/', lambda request: render(request, 'customers.html'), name='customers'),
    path('orders/', lambda request: render(request, 'orders.html'), name='orders'),
]