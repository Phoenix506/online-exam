from django.shortcuts import render


# Create your views here.


def index_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def account_page(request):
    return render(request, 'account.html')


def contact(request):
    return render(request, 'contact.html')


