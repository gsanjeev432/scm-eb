from django.urls import path

from . import views

urlpatterns = [
    path('', views.manufacturer_list, name='manufacturer_list'),
    path('add/', views.add_manufacturer, name='add_manufacturer'),
    path('<int:manufacturer_id>/products/', views.product_list, name='product_list'),
    path('<int:manufacturer_id>/products/add/', views.add_product, name='add_product'),
]
