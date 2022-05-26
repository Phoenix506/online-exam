from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import UserRegistrationForm, UserLoginForm


# Create your views here.


def register(request):
    context = {}
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form'] = form
    else:
        form = UserRegistrationForm()
        context['register_form'] = form
    return render(request, 'user/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    context = {}
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
        else:
            context['login_form'] = form
    else:
        form = UserLoginForm
        context['login_form'] = form
    return render(request, 'account.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
