from django.urls import path
from . import views
from login_singup_page import views as login_views

urlpatterns = [
    path('', views.index),
    path('login/', login_views.login),
    path('reg/', login_views.registration)
]
