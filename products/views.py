from django.shortcuts import render

# Create your views here.

def product_views(request):
    return render(request, 'product_views.html')

def product_details(request):
    return render(request, 'product_details.html')