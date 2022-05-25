from django.shortcuts import render


def login(request):
    return render(request, 'login_singup_page/login_page.html')

def registration(request):
    return render(request, 'login_singup_page/reg_page.html')
