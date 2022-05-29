"""online_exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import index_page, about_page, account_page, contact, result_exams, result_tests
from user.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('user/', include('user.urls')),
    path('exams/', include('exams.urls')),
    path('about/', about_page, name='about'),
    path('account/', account_page, name='account'),
    path('profile/exams/', result_exams, name='result_exams'),
    path('profile/tests/', result_tests, name='result_tests'),
    path('profile/', profile, name='profile'),
    path('contact/', contact, name='contact'),
]
