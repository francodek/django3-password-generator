from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    charaters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charaters.extend(list('ABCDEFGHIJKLMNOPKRSTUVWXYZ'))
    if request.GET.get('special'):
        charaters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        charaters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charaters)


    return render(request, 'generator/password.html', {'password': thepassword})

