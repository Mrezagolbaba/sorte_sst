from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Packages, SelectedPackage, Reservation, LiveSession, Tradeidea
import re
from django.contrib import messages

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


def trade_idea(request):
    ideas = Tradeidea.objects.all().order_by('-id')
    context = {
        'ideas':ideas
    }
    return render(request, 'membership/tradeidea.html', context)



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




def oneonone_reservation(request):
    reservables = Reservation.objects.order_by('-id').filter(status='Open')
    context = {
        'reservables': reservables
    }
    return render(request, 'membership/reservation.html', context)



def oneonone_reservation_detail(request, session_id):
    live_oneonone = get_object_or_404(Reservation, id=session_id)
    context = {
        'live_oneonone': live_oneonone
    }
    return render(request, 'membership/oneonone_reservation_detail.html', context)



def oneonone_make_reservation(request, session_id):
    user = request.user
    reservation = Reservation.objects.get(id=session_id)
    check_for_repeat = LiveSession.objects.all().filter(reservation=reservation, user=user)

    if not check_for_repeat:
        reservation.free_users = reservation.free_users - 1
        messages.info(request, 'your reservation is saved')
        reservation.save() 
        LiveSession.objects.create(reservation=reservation, user=user)            

        if reservation.free_users == 0:
            reservation.status=2
            reservation.save()
    else:
         messages.info(request, 'you can not reserve for second time')    

    return render(request,'membership/oneonone_reservation_detail.html')





