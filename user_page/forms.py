from email_validate import validate

import django.contrib.auth.forms as auth_form
import django.contrib.auth.models as auth_model
from django import forms
from django.forms import TextInput, FileInput

from .models import UserUsdAcc, UserCryptoAcc, UsersAvatars

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
                'placeholder': 'Имя',
                'value': '',
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

    def is_valid(self) -> bool:
        first_name, last_name, email = self.data["first_name"], self.data["last_name"], self.data["email"]

        for symbol in first_name:
            if not str.isalpha(symbol):
                return False

        for symbol in last_name:
            if not str.isalpha(symbol):
                return False

        if not validate(email_address=email, check_format=True, check_blacklist=True, check_dns=True, dns_timeout=10,
                        check_smtp=False, smtp_debug=False):
            return False

        return True


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


class UserAvatarForm(forms.ModelForm):
    class Meta:
        model = UsersAvatars
        fields = ["imgur_link"]
        widgets = {
            'imgur_link': FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'id': 'avatar',
            })}
