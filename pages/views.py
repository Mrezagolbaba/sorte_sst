from django.shortcuts import render, redirect
from .models import NewsletterModel, ContactModel

def index(request):
    return render(request, 'pages/index.html')


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