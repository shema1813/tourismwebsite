from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.
def homepage(request ):
    return render  (request,"index.html")

def loginpage(request ):
    print("you did a"+request.method)
    if request.method == "POST":
        print(request.POST)
        typedname = request.POST.get("username")
        print("the name you typed is :" + typedname)
        typedpassword =request.POST.get("password")
       
        result= authenticate(username=typedname,password=typedpassword)
        if result == None:
            return HttpResponse("you are't registered with us" )
        else:
            login(request,result)
            return redirect("homepage")
    return render  (request,"signin.html")


    
def signuppage (request) :
    if request.method == "POST":
        print(request.POST)
        typedname = request.POST.get("username")
        print("the name you typed is :" + typedname)
        typedpassword =request.POST.get("password")
        print("your password is :" + typedpassword)
        typedemail = request.POST.get("email")
        print("your email is :" + typedemail)
        typedfirstname = request.POST.get("Firstname")
        print("your firstname is :" + typedfirstname)
        typedLastname = request.POST.get("Lastname")
        print("your last name is :" + typedLastname)
        newpassword = make_password(typedpassword)
        Newuser=User(password=newpassword,username=typedname,last_name=typedLastname,email=typedemail,first_name=typedfirstname)
        Newuser.save()
    return render (request,"signup.html")
