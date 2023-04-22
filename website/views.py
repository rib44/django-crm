from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html', {})
    

def login_user(request):
    # Check to see if loggin in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error, Please Try Again...")
            return redirect('home')

    
    return render(request, 'login.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return render(request, 'logout.html', {})

def register_user(request):
    return render(request, 'register.html', {})
