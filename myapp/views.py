from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from myapp.models import customers
import pyodbc

from myproject.settings import DATABASES


def database(request):
    if request.method=="POST":
        if request.POST.get('username') and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') :
            inserted_values=customers #customer data is stored in inserted_values
            inserted_values.username= request.POST.get('username')
            inserted_values.first_name= request.POST.get('first_name')
            inserted_values.last_name= request.POST.get('last_name')
            inserted_values.email= request.POST.get('email')
      #to inset data into DB we need to use cursor method which is used to execute select stmts or queries of sql
            cursor=DATABASES.cursor()
            cursor.execute("insert into customers values('"+inserted_values.username+"','"+inserted_values.first_name+"','"+inserted_values.last_name+"','"+inserted_values.email+"')") 
            cursor.commit()
            return render(request,'myapp/index.html')
    else:
            return render(request,'myapp/index.html')

def home(request):
    return render(request,"myapp/index.html")

def signup(request):
    #to collect data posted by user nd store in DB
    if request.method=="POST":
        Username=request.POST['username']
        FirstName=request.POST['first_name']
        LastName=request.POST['last_name']
        Email=request.POST['email']
        Password=request.POST['pass1']
        ConfirmPassword=request.POST['pass2']

        

        myuser = User.objects.create_user(Username,Email,Password) #create user with this info
        myuser.first_name=FirstName
        myuser.last_name=LastName

        myuser.save()  #to save the user
        messages.success(request,"your account is successfuly created")  #to print a msg after successful signup

        return redirect('signin')
    return render(request,"myapp/signup.html")

def signin(request):

    if request.method=="POST":
        Username=request.POST['username']
        Password=request.POST['pass1']

        user=authenticate(Username=Username, Password=Password)

        if user is not None:
            login(request,user)
            return redirect('imagesPage')
        else:
            messages.error(request,"wrong credentials")
            return redirect('home')
    return render(request,"myapp/signin.html")

def signout(request):
    pass

def imagesPage(request):
    return render(request,"myapp/imagesPage.html")

def animals(request):
    return render(request,"myapp/animals.html")

def basic(request):
    return render(request,"myapp/basic.html")

def medium(request):
    return render(request,"myapp/medium.html")

def advanced(request):
    return render(request,"myapp/advanced.html")

def alphabets(request):
    return render(request,"myapp/alphabets.html")

def alphabets_small(request):
    return render(request,"myapp/alphabets_small.html")

def alphabets_capital(request):
    return render(request,"myapp/alphabets_capital.html")

def numbers(request):
    return render(request,"myapp/numbers.html")

def numbers_zero_nine(request):
    return render(request,"myapp/numbers_zero_nine.html")

def numbers_words(request):
    return render(request,"myapp/numbers_words.html")

def shapes(request):
    return render(request,"myapp/shapes.html")

def shapes_and_names(request):
    return render(request,"myapp/shapes_and_names.html")

def colors(request):
    return render(request,"myapp/colors.html")

def states(request):
    return render(request,"myapp/states.html")

def indian_states(request):
    return render(request,"myapp/indian_states.html")

def indian_capitals(request):
    return render(request,"myapp/indian_capitals.html")




