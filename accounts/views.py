from multiprocessing import context
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_
from django.contrib.auth.models import User
from .models import DiscordModel
from membership.models import LiveSession, SelectedPackage
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
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

@login_required(login_url='login')
def discord(request):
    discord_user = DiscordModel.objects.all().filter(user=request.user)
    context = {
        'discord_user':discord_user
    }
    return render(request, 'accounts/discord.html', context)

def discord_save(request):
    if request.method == 'POST':
        user = request.user
        email = user.email
        discord_id = request.POST['discord_id']
        check_for_repeat = DiscordModel.objects.all().filter(discord_id=discord_id)
        if not check_for_repeat:
            discord = DiscordModel.objects.create(user=user, email=email,discord_id=discord_id)
            discord.save()
            
        else:
            messages.info(request, 'you can not reserve for second time')
            return redirect('discord')
    return redirect('discord')

    # return redirect('discord')
@login_required(login_url='login')
def bookings(request):
    bookings = LiveSession.objects.all().filter(user=request.user)
    context = {
        'bookings': bookings,
    }    
    return render(request, 'accounts/bookings.html', context)


@login_required(login_url='login')
def bought_package(request):
    membership = SelectedPackage.objects.all().filter(user=request.user)
    context = {
        'membership': membership
    }
    return render(request,'accounts/dashboard-memberships.html', context)









