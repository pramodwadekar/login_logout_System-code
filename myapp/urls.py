from django.urls import path
from . import views

urlpatterns = [
    path("",views.RegisterPage, name="registerpage"),
    path("register/", views.UserRegister, name = "register"),
    path("loginpage/", views.loginpage, name = "loginpage"),
    path("loginuser/", views.LoginUser, name = "login"),

]