
from django.urls import path 
from . import views


urlpatterns = [
    path('details/',views.product_details,name='product_details'),
    path('views/<int:user_id>/',views.product_views,name='product_view')  ,
    path('create/<int:user_id>/',views.create_product,name='create_product')

] 
