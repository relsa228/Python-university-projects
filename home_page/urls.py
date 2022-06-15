from django.urls import path
from . import views
from login_singup_page import views as login_views

urlpatterns = [
    path('', views.index),
    path('eth_overview/', views.eth_overview),
    path('ltc_overview/', views.ltc_overview),
    path('xrp_overview/', views.xrp_overview),
    path('dash_overview/', views.dash_overview),
    path('zec_overview/', views.zec_overview),

    path('logout/', views.logout_user),
    path('login/', login_views.CustLoginView.as_view(), name='login'),
    path('reg/', login_views.RegistrationView.as_view(), name='register')
]
