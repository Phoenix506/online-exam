from django.shortcuts import render

# Create your views here.
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
        return redirect('profile')
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


@login_required(login_url='/user/login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/user/login')
def profile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Məlumatlarınız yeniləndi')
            return redirect('index')
    else:
        u_form = forms.UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'profile.html', context)
