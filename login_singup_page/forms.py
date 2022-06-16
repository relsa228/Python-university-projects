from django.forms import TextInput, PasswordInput
import django.contrib.auth.forms as auth_form
import django.contrib.auth.models as auth_model
from django import forms

from login_singup_page.models import VerificateUser


class RegUsersForm(auth_form.UserCreationForm):
    class Meta:
        model = auth_model.User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'firstName',
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
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'id': 'password1',
                'required': True
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'id': 'password2',
                'required': True
            }),
        }


class LogUsersForm(auth_form.AuthenticationForm):
    fields = ['username', 'password']
    widgets = {
        'username': TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'Имя пользователя',
            'required': True
        }),
        'password': PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'id': 'floatingPassword',
            'placeholder': 'Пароль',
            'required': True
        }),
    }


class VerificationForm(forms.ModelForm):
    class Meta:
        model = VerificateUser
        fields = ['username', 'is_verificate']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'id': 'username',
                'placeholder': 'Имя пользователя',
                'required': True
            }),
            'is_verificate': TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'id': 'verification_code',
                'placeholder': 'Код верификации',
                'required': True
            }),
        }
