
from django.urls import path 
from . import views


urlpatterns = [
    path('details/',views.product_details,name='product_details'),
    path('views/',views.product_views,name='product_views')   

] 
