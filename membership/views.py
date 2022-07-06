from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Packages, SelectedPackage
import re

@login_required(login_url='login')
def all_memberships(request):
    return render(request, 'membership/all_memberships.html')


def monthly_checkout(request):
    package = Packages.objects.all().filter(title='Monthly')
    context = {
        'package':package
    }
    return render(request, 'membership/monthly_checkout.html', context)

def bronze_checkout(request):
    package = Packages.objects.all().filter(title='Bronze')
    context = {
        'package':package
    }
    return render(request, 'membership/bronze_checkout.html', context)
 
def silver_checkout(request):
    package = Packages.objects.all().filter(title='Silver')
    context = {
        'package':package
    }
    return render(request, 'membership/silver_checkout.html', context)
 
def gold_checkout(request):
    package = Packages.objects.all().filter(title='Gold')
    context = {
        'package':package
    }
    return render(request, 'membership/gold_checkout.html', context)
 
def lifetime_checkout(request):
    package = Packages.objects.all().filter(title='Lifetime')
    context = {
        'package':package
    }
    return render(request, 'membership/lifetime_checkout.html', context)
 

def signalonly_checkout(request):
    package = Packages.objects.all().filter(title='Signal only')
    context = {
        'package':package
    }
    return render(request, 'membership/signalonly_checkout.html', context)




def save_selected_package(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        str_price = request.POST['price']
        temp = re.findall(r'\d+', str_price)
        price = list(map(int,temp))
        left_value = str(price[0])
        right_value = str(price[1])
        price = left_value + "." + right_value 
        package = SelectedPackage.objects.create(user=user, title=title, price=price)
        package.save()
        return redirect('index')
















