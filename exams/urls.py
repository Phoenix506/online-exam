from django.urls import path
from .views import exams_page, take_exam

urlpatterns = [
    path('index/', exams_page, name='exams-index'),
    path('exam/', take_exam, name='take_exam'),

]
