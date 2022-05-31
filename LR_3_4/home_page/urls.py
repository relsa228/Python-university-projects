from django.urls import path
from . import views
from login_singup_page import views as login_views

urlpatterns = [
    path('', views.index),
    path('logout/', views.logout_user),
    path('login/', login_views.CustLoginView.as_view(), name='login'),
    path('reg/', login_views.RegistrationView.as_view(), name='register')
]
