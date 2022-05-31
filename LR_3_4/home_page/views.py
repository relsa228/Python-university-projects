import requests as requests
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def index(request):
    #print(requests.get(url="https://api.exmo.com/v1.1/ticker/").text)
    return render(request, 'home_page/index.html')


def logout_user(request):
    logout(request)
    return redirect('/./')
