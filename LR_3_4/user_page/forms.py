from urllib import request

import django.contrib.auth.forms as auth_form
import django.contrib.auth.models as auth_model
from .models import UserUsdAcc, UserCryptoAcc
from django import forms
from django.forms import TextInput

TICKERS = [
    ('BTC', 'BTC_USD'),
    ('ETH', 'ETH_USD'),
    ('XRP', 'XRP_USD'),
    ('LTC', 'LTC_USD'),
    ('ZEC', 'ZEC_USD'),
    ('DASH', 'DASH_USD'),
]


class RedactForm(auth_form.UserChangeForm):
    class Meta:
        model = auth_model.User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'firstName',
                'value': 'th',
                'placeholder': 'Имя',
                'required': True
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'lastName',
                'placeholder': 'Фамилия',
                'required': True
            }),
            'username': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'username',
                'placeholder': 'Имя пользователя',
                'required': True
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'email',
                'placeholder': 'you@example.com',
                'required': True
            }),
        }


class UsdDepositForm(forms.ModelForm):
    class Meta:
        model = UserUsdAcc
        fields = ['usd_count']
        widgets = {
            'usd_count': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': 'usdDeposit',
            })}


class CryptoForm(forms.ModelForm):
    class Meta:
        model = UserCryptoAcc
        fields = ["crypto_ticker", "token_count"]
        widgets = {
            'token_count': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': 'usdDeposit',
            }),

            'crypto_ticker': forms.Select(choices=TICKERS)}
