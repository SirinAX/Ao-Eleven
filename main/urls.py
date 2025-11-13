from django.urls import path
from . import views
from main.views import register,login_user,logout_user
from main.views import edit_product_ajax
from main.views import add_product_ajax,proxy_image,create_product_flutter
app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('delete-product/<int:pk>/', views.delete_product_ajax, name='delete_product_ajax'),
    path('add-employee/',views.add_employee,name = 'add_employee'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
path('edit-product-ajax/<int:pk>/', views.edit_product_ajax, name='edit_product_ajax'),
     path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
     path('products/list/ajax/', views.products_list_ajax, name='products_list_ajax'),
      path('proxy-image/', proxy_image, name='proxy_image'),
      path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    
    

    # Export JSON/XML
    path('products/json/', views.products_json, name='products_json'),
    path('products/xml/', views.products_xml, name='products_xml'),
    path('products/json/<int:pk>/', views.product_json, name='product_json'),
    path('products/xml/<int:pk>/', views.product_xml, name='product_xml'),
]
