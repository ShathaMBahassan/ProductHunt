from django.shortcuts import render , redirect
from .models import Product 
from Users.models import Create_User
from django.contrib import messages

# Create your views here.

def product_views(request,user_id):
    products = Product.objects.filter(hunter_id=user_id)
    return render(request, 'product_views.html',{'user_id':user_id,'products':products})

def product_details(request):

    return render(request, 'product_details.html')

def create_product(request,user_id):
    if request.method == 'POST':

        pro_name_inp = request.POST.get('product_name')
        pro_link_inp = request.POST.get('product_link')
        pro_logo_inp = request.FILES.get('product_logo')
        pro_des_inp = request.POST.get('description')
        pro_date_inp = request.POST.get('product_date')



        try:
            pro_info = Product.objects.get(
                tilte=pro_name_inp,
                url=pro_link_inp,
                image=pro_logo_inp,
                body=pro_des_inp,
                pub_date=pro_date_inp,
                hunter_id= user_id
            )

        except Product.DoesNotExist:

            new_pro = Product.objects.create(
                tilte=pro_name_inp,
                url=pro_link_inp,
                image=pro_logo_inp,
                body=pro_des_inp,
                pub_date=pro_date_inp,
                hunter_id=user_id
            )
            
            messages.success(request, 'Product created successfully')
            return redirect('product_view', user_id=user_id)

    return render(request, 'create_product.html' , {'user_id':user_id})