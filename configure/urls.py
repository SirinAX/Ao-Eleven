from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Product views
    path('products/add/', views.product_add, name='product_add'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    # Export JSON/XML
    path('products/json/', views.products_json, name='products_json'),
    path('products/xml/', views.products_xml, name='products_xml'),
    path('products/json/<int:pk>/', views.product_json, name='product_json'),
    path('products/xml/<int:pk>/', views.product_xml, name='product_xml'),
]

# untuk development: media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
