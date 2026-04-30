from django.shortcuts import render , redirect
from .models import Create_User
from django.contrib.auth import logout



def login(request):
    if request.method == 'POST':
        username_inp = request.POST['username']
        password_inp = request.POST['password'] 
        try:
            user = Create_User.objects.get(
                username=username_inp,
                Password=password_inp)
            
            request.session['username'] = username_inp

            return redirect('product_views')
        except Create_User.DoesNotExist:
            message = 'Invalid username or password'
            return render(request,'login.html',{'error_login':message})
    else:
        return render(request,'login.html')

def signUp(request):
    if request.method =='POST':
        # User enter the info
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = Create_User.objects.get(username=request.POST['username'])
                user_message = "the user has been already exist"
                return render(request,'signUp.html',{'error_user':user_message})
            except Create_User.DoesNotExist:
                user = Create_User.objects.create(
                    username= request.POST['username'],
                    Password = request.POST['password1']
                )
                return render(request,'message.html')
        else:
            message = "Password and confirmation do not match."
            return render(request,'signUp.html', {'error_password': message})

    else:
        # User didn't add info
        return render(request,'signUp.html')



def logOut(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'login.html') 
        

    return redirect('product_views')


