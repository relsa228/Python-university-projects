from django.urls import path
from user_page import views as user_views
from . import views as log_reg_views
from .views import emal_aprove

urlpatterns = [
    path('user/', user_views.ProfileView.as_view()),
    path('reg/email_aprove/', emal_aprove),
    path('reg/verificate_email/', log_reg_views.VerificationView.as_view())
]
