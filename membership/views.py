from ast import parse
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Packages, SelectedPackage, Reservation, LiveSession, Tradeidea
import re
from django.contrib import messages
from dateutil.relativedelta import relativedelta
import datetime
from django.utils.dateparse import parse_datetime
import dateutil.parser



@login_required(login_url='login')
def all_memberships(request):
    return render(request, 'membership/all_memberships.html')


def monthly_checkout(request):
    current_datetime = datetime.datetime.now()
    end_date = current_datetime + relativedelta(months=1)
    package = Packages.objects.all().filter(title='Monthly')
    context = {
        'package':package,
        'current_datetime':current_datetime,
        'end_date': end_date,
    }
    return render(request, 'membership/monthly_checkout.html', context)

def bronze_checkout(request):
    current_datetime = datetime.datetime.now()
    end_date = current_datetime + relativedelta(months=3)
    package = Packages.objects.all().filter(title='Bronze')
    context = {
        'package':package,
        'current_datetime':current_datetime,
        'end_date': end_date,
    }
    return render(request, 'membership/bronze_checkout.html', context)
 
def silver_checkout(request):
    current_datetime = datetime.datetime.now()
    end_date = current_datetime + relativedelta(months=6)
    package = Packages.objects.all().filter(title='Silver')
    context = {
        'current_datetime':current_datetime,
        'package':package,
        'end_date':end_date
    }
    return render(request, 'membership/silver_checkout.html', context)
 
def gold_checkout(request):
    current_datetime = datetime.datetime.now()
    end_date = current_datetime + relativedelta(months=12)
    package = Packages.objects.all().filter(title='Gold')
    context = {
        'current_datetime':current_datetime,
        'package':package,
        'end_date': end_date
    }
    return render(request, 'membership/gold_checkout.html', context)
 
def lifetime_checkout(request):
    current_datetime = datetime.datetime.now()
    package = Packages.objects.all().filter(title='Lifetime')
    context = {
        'current_datetime':current_datetime,
        'package':package
    }
    return render(request, 'membership/lifetime_checkout.html', context)
 

def signalonly_checkout(request):
    current_datetime = datetime.datetime.now()
    end_date = current_datetime + relativedelta(months=1)
    package = Packages.objects.all().filter(title='Signal only')
    context = {
        'current_datetime':current_datetime,
        'package':package,
        'end_date': end_date
    }
    return render(request, 'membership/signalonly_checkout.html', context)


def trade_idea(request):
    current_datetime = datetime.datetime.now()
    ideas = Tradeidea.objects.all().order_by('-id')
    context = {
        'current_datetime':current_datetime,
        'ideas':ideas
    }
    return render(request, 'membership/tradeidea.html', context)



def save_selected_package(request):
    current_datetime = datetime.datetime.now()
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        if title == 'Bronze':
            end_date =  current_datetime + relativedelta(months=3)
        elif title == 'Gold':
            end_date =  current_datetime + relativedelta(months=12)
        elif title == 'Silver':
            end_date =  current_datetime + relativedelta(months=6)
        elif title == 'Monthly':
            end_date =  current_datetime + relativedelta(months=1)
        elif title == 'Signal only':
            end_date =  current_datetime + relativedelta(months=1)
        str_price = request.POST['price']
        temp = re.findall(r'\d+', str_price)
        price = list(map(int,temp))
        left_value = str(price[0])
        right_value = str(price[1])
        price = left_value + "." + right_value 
        package = SelectedPackage.objects.create(user=user, title=title, price=price, start_date=current_datetime, end_date=end_date)
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





