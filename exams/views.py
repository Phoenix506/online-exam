from django.shortcuts import render


# Create your views here.

def exams_page(request):
    return render(request, 'exams.html')


def take_exam(request):
    return render(request, 'take_exam.html')

