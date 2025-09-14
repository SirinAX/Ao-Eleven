from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('products/add/', views.product_add, name='add_product'),
    path('products/<int:pk>/', views.product_detail, name='show_detail'),

    # Export JSON/XML
    path('products/json/', views.products_json, name='products_json'),
    path('products/xml/', views.products_xml, name='products_xml'),
    path('products/json/<int:pk>/', views.product_json, name='product_json'),
    path('products/xml/<int:pk>/', views.product_xml, name='product_xml'),
]
