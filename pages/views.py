from django.shortcuts import render, redirect
from .models import NewsletterModel

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