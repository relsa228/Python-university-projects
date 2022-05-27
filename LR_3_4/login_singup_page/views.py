from django.shortcuts import render
from .forms import UsersForm
from .models import Users


def login(request):
    return render(request, 'login_singup_page/login_page.html')


def registration(request):
    if request.method == "POST":
        user_form_save = UsersForm(request.POST)
        if user_form_save.is_valid():
            user_form_save.save()
        else:
            print(user_form_save.errors)

    user_form = UsersForm()
    data = {
        'forms': user_form
    }
    return render(request, 'login_singup_page/reg_page.html', data)
