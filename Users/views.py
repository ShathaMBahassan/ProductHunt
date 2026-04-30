from django.shortcuts import render
from .models import Create_User


def login(request):

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

    return render(request,'logOut.html')


