from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from .forms import RegUsersForm, LogUsersForm
from .utils import create_user_crypto_bills, create_user_usd_bill, create_avatar_link, send_aprove_mail


class EmalAprove(CreateView):
    success_url = "/./user/"
    form_class = RegUsersForm
    template_name = 'login_singup_page/email_aprove_page.html'


class RegistrationView(CreateView):
    success_url = 'email_aprove/'
    form_class = RegUsersForm
    template_name = 'login_singup_page/reg_page.html'

    def post(self, request):
        res_form = RegUsersForm(request.POST)
        if res_form.is_valid():
            create_avatar_link(request.POST["username"])
            create_user_crypto_bills(request.POST["username"])
            create_user_usd_bill(request.POST["username"])
            request.user.username = request.POST["username"]
            send_aprove_mail(request.POST["email"], request.POST["username"], request.POST["first_name"], request.POST["last_name"])
        return super(RegistrationView, self).post(request)


class CustLoginView(LoginView):
    form_class = LogUsersForm
    template_name = 'login_singup_page/login_page.html'

    def get_success_url(self):
        return '/./user/'
