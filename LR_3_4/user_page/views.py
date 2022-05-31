from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import RedactForm


class RedactUserView(CreateView):
    success_url = ''
    form_class = RedactForm
    template_name = 'user_page/profile.html'


def deposit(request):
    return render(request, 'user_page/deposit.html')


def wallet(request):
    return render(request, 'user_page/wallet.html')


def profile(request):
    return render(request, 'user_page/profile.html')
