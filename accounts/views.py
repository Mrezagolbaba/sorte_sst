from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_
from django.contrib.auth.models import User



def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    logout_(request)
    return redirect('index')


def register(request):
    if request.method == "POST":
        #Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'this email is being used')
                    return redirect('registr')
                else:
                    #looks good
                    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    user.save()
                    auth.login(request, user)
                    return redirect('dashboard')
        
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password=password)
       if user is not None:
           auth.login(request, user)
           messages.success(request, 'You are now logged in')
           return redirect('dashboard')
    
    return render(request, 'accounts/login.html')


















