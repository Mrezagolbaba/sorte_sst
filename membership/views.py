from ast import parse
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Packages, SelectedPackage, Reservation, LiveSession, Tradeidea
import re
from django.contrib import messages
from dateutil.relativedelta import relativedelta
import datetime
from datetime import date
from django.core.mail import send_mail
from accounts.models import DiscordModel


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
        mail = user.email
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
        package = SelectedPackage.objects.create(user=user, title=title, price=price, start_date=current_datetime, end_date=end_date, email=mail)
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



def ten_days_left_members(request):
    all_users = SelectedPackage.objects.all()
    context = None
    today = date.today()
    past_due = False
    zero_days = False
    list_search_by_email = []
    for member in all_users:
        expire_date = getattr(member, 'end_date').date()
        b = expire_date - today
        b = str(b)    
        
        if today > expire_date:
    
                send_mail(
                    'Reminder',
                    'your account has been expired  ' + 'in last ' + ' ' +str(today - expire_date) ,
                    'amirhosein.ai92@gmail.com',
                    [member.email, 'amir.cpu@gmail.com'],
                    fail_silently=False
                )
                list_search_by_email.append(member.email)    
                pass
        if today < expire_date:

            if int(b[0]) == 0:
              zero_days = True  
            if int(b[0]) <= 10 :
                ten_days_left = True

        
            if zero_days:
                # list_users += member
                send_mail(
                    'Reminder',
                    'your account has been expired  ',
                    'amirhosein.ai92@gmail.com',
                    [member.email, 'amir.cpu@gmail.com'],
                    fail_silently=False
                )
                list_search_by_email.append(member.email)
        
    
            if ten_days_left:
               days_left = int(b[0:2])

               if days_left <= 10:

                # list_users += member
                send_mail(
                    'Reminder',
                    'your account will be expired in ' + str(days_left)+ ' days',
                    'amirhosein.ai92@gmail.com',
                    [member.email, 'amir.cpu@gmail.com'],
                    fail_silently=False
                )
                list_search_by_email.append(member.email)

             

    
    for item in list_search_by_email:
        expired_users = SelectedPackage.objects.all().filter(email=item)
        discord_username = DiscordModel.objects.all().filter(email=item)
        # print(item)

    context = {
        'expired_users':expired_users,
        'discord_username': discord_username
    }

    return render(request, 'membership/ten_days.html', context)
        

# def oreder//////