from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile),
    path('wallet/', views.wallet),
    path('deposit/', views.deposit),
    path('edit_profile/', views.edit)
]
