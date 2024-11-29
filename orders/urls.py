from django.urls import path

from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.create_order, name='create_order'),
    path('<int:order_id>/', views.order_details, name='order_details'),
    path('<int:order_id>/update/', views.update_order_status, name='update_order_status'),
]
