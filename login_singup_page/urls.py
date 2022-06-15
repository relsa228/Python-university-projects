from django.urls import path
from user_page import views as user_views
from . import views as log_reg_views

urlpatterns = [
    path('user/', user_views.ProfileView.as_view()),
    path('reg/email_aprove', log_reg_views.EmalAprove.as_view()),
]
