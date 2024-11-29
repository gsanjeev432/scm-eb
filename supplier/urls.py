from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('add/', views.add_supplier, name='add_supplier'),
    path('<int:supplier_id>/materials/', views.raw_materials_list, name='raw_materials_list'),
    path('<int:supplier_id>/materials/add/', views.add_raw_material, name='add_raw_material'),
]
