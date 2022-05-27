from .models import Users
from django.forms import ModelForm, TextInput, ChoiceField, Select


class UsersForm(ModelForm):
    class Meta:
        model = Users

        fields = ['first_name', 'last_name', 'nickname', 'email', 'adress', 'country']
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
            'nickname': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'username',
                'placeholder': 'Никнейм',
                'required': True
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'email',
                'placeholder': 'you@example.com',
                'required': True
            }),
            'adress': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'address',
                'placeholder': 'Адрес',
                'required': True
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'id': 'country',
                'placeholder': 'Страна',
                'required': True
            }),
        }
