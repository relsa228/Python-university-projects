from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileView.as_view()),
    path('wallet/', views.WalletView.as_view()),
    path('deposit/', views.DepositView.as_view()),
    path('buy/', views.buy),
    path('sell/', views.sell),
    path('edit_profile/', views.RedactUserView.as_view())
]
