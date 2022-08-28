from multiprocessing import context
from django.shortcuts import render, redirect
from .models import NewsletterModel, ContactModel
from event.models import Event
from datetime import date, datetime

def index(request):
    # today = date.today()
    today = datetime.now().strftime ("%d%-H%M%-S")
    b = today
    today  = str(today)
    today_day = today[0:2]
    when_ts_d=None
    when_ts_hours=None
    when_ts_min=None
    when_ts_sec=None
    when_ls_d=None
    when_ls_hours=None
    when_ls_min=None
    when_ls_sec=None
    when_ny_d=None
    when_ny_hours=None
    when_ny_min=None
    when_ny_sec=None
    tokyo_session = Event.objects.all().filter(title='Tokyo Session', status='Upcoming')
    for ts in tokyo_session:
        when_ts_d =ts.when.strftime ("%d")
        when_ts_hours =ts.when.strftime ("%-H")
        when_ts_min =ts.when.strftime ("%M")
        when_ts_sec =ts.when.strftime ("%-S")
    
    

    london_session = Event.objects.all().filter(title='London Session', status='Upcoming')
    for ls in london_session:
        when_ls_d =ls.when.strftime ("%d")
        when_ls_hours =ls.when.strftime ("%-H")
        when_ls_min =ls.when.strftime ("%M")
        when_ls_sec =ls.when.strftime ("%-S")
    
    
    ny_session = Event.objects.all().filter(title='NY Session', status='Upcoming')
    for ny in ny_session:
        when_ny_d =ny.when.strftime ("%d")
        when_ny_hours =ny.when.strftime ("%-H")
        when_ny_min =ny.when.strftime ("%M")
        when_ny_sec =ny.when.strftime ("%-S")
    
    ts_dict = {'when_ts_d':when_ts_d, 'when_ts_hours':when_ts_hours, 'when_ts_min':when_ts_min, 'when_ts_sec':when_ts_sec}
    ls_dict = {'when_ls_d':when_ls_d, 'when_ls_hours':when_ls_hours, 'when_ls_min':when_ls_min, 'when_ls_sec':when_ls_sec}
    ny_dict = {'when_ny_d':when_ny_d, 'when_ny_hours':when_ny_hours, 'when_ny_min':when_ny_min, 'when_ny_sec':when_ny_sec}
    
    context = {
        'tokyo_session': tokyo_session,
        'london_session':london_session,
        'ny_session':ny_session,
        'ts_dict':ts_dict,
        'ls_dict': ls_dict,
        'ny_dict': ny_dict,
    }

    return render(request, 'pages/index.html', context)


def contact_us(request):
    return render(request, 'pages/contactus.html')


def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        subscriber = NewsletterModel(user= request.user,email=email)
        subscriber.save()
    return redirect('index')

def send_message_to_admin(request):
    if request.method == 'POST':
        name_ = request.POST['full_name']
        number = request.POST['number']
        email = request.POST['email']
        msg = request.POST['message']
        contact = ContactModel(full_name=name_, number=number, email=email, message=msg)
        contact.save()
    return redirect('index')


    
   