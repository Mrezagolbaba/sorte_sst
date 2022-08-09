from django.shortcuts import render, redirect
from pages.models import NewsletterModel

def store_homepage(request):
    return render(request, 'store/store.html')



def store_newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        subscriber = NewsletterModel(user= request.user,email=email)
        subscriber.save()
    return redirect('index')