
from django.urls import path
from . import views


urlpatterns = [
    path("login/",views.login,name='login_page'),
    path("signUp/",views.signUp,name="singUp_page"),
    path("logOut/",views.logOut,name="logOut_page")
] 