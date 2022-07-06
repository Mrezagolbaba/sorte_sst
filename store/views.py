from django.shortcuts import render


def store_homepage(request):
    return render(request, 'store/store.html')