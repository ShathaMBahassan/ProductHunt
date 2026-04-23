
from django.contrib import admin
from django.urls import path , include 
from django.conf.urls.static import static 
from django.conf import settings
import Users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Users/',include('Users.urls')),
    path('Products/',include('products.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
