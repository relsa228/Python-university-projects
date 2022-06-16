from django.contrib import admin
from django.urls import path, include
from login_singup_page import views as log_reg_views
from login_singup_page.views import emal_aprove

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('user/', include('user_page.urls')),
    path('reg/email_aprove/', emal_aprove),
    path('reg/verificate_email/', log_reg_views.VerificationView.as_view())
]
