from django.urls import path
from . import views
from main.views import register,login_user,logout_user
from main.views import edit_product

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:pk>/confirm_delete/', views.product_confirm_delete, name='product_confirm_delete'),
    path('add-employee/',views.add_employee,name = 'add_employee'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("news/<int:id>/edit", views.edit_product, name="edit_product"),
    

    # Export JSON/XML
    path('products/json/', views.products_json, name='products_json'),
    path('products/xml/', views.products_xml, name='products_xml'),
    path('products/json/<int:pk>/', views.product_json, name='product_json'),
    path('products/xml/<int:pk>/', views.product_xml, name='product_xml'),
]
