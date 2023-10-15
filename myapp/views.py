from django.shortcuts import render
from .models import *

# Create your views here.

# view for register page
def RegisterPage(request):
    return render(request, "register.html")


# view for user register
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password= request.POST['password']
        cpassword = request.POST['cpassword']


        # First we will validate thet user already exist
        user = User.objects.filter(Email = email)
        if user:
            message = "User already Exist....." 
            return render(request, "register.html", {'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname = fname, Lastname = lname, Email = email, 
                                              Contact = contact, Password =password)
                message = "User Register Successfully"
                return render(request, "login.html", {"msg":message})
            
            else:
                message = "Password or confirm Password Doesn't Match"
                return render(request, "register.html", {"msg":message})
            
def loginpage(request):
    return render(request, "login.html")


def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password'] 
        
        #Checking email id with database 
        user = User.objects.get(Email = email) 
        if user:
            if user.Password == password:
                request.session["Firstname"] = user.Firstname
                request.session["Lastname"] = user.Lastname        
                request.session["Email"] = user.Email   
                request.session["Contact"] = user.Contact 
                return render(request, "home.html")
            else:
                message ="Password Does Not Match"
                return render(request, "login.html",{"msg":message})
        else:
            message = "User Does Not Exist"
            return render(request, "register.html",{"msg":message})



