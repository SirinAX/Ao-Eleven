from django.contrib import admin
from django.urls import path
from main.views import home
from django.conf import settings
from django.conf.urls.static import static
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('product/<int:pk>/', views.product_detail, name='product_detail'),
]

# untuk development: media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
