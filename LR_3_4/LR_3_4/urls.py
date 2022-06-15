from django.contrib import admin
from django.urls import path, include
from login_singup_page import views as log_reg_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('user/', include('user_page.urls')),
    path('reg/email_aprove/', log_reg_views.EmalAprove.as_view())
]
