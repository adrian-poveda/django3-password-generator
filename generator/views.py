from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html',{'password':'adrianpwd'})

def password(request):
    generated_password = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('lenght', 12))

    uppercase = request.GET.get('uppercase', False)

    special = request.GET.get('special', False)

    numbers = request.GET.get('numbers', False)

    if uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if special:
        characters.extend(list('!@#%&/()*[]+-:'))
    
    if numbers:
        characters.extend(list('0123456789'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})
