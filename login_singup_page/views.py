from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from .forms import RegUsersForm, LogUsersForm, VerificationForm
from .utils import create_user_crypto_bills, create_user_usd_bill, create_avatar_link, send_aprove_mail, \
    verificate_user, verifiction_check


class VerificationView(CreateView):
    success_url = '/./reg/email_aprove/'
    form_class = VerificationForm
    template_name = 'login_singup_page/email_verificate_form.html'

    def post(self, request, *args, **kwargs):
        code = request.POST["is_verificate"]
        if verificate_user(code):
            return redirect("/./reg/email_aprove/")
        else:
            return super(VerificationView, self).post(request)


def emal_aprove(request):
    return render(request, 'login_singup_page/email_aprove_page.html')


class RegistrationView(CreateView):
    success_url = 'verificate_email/'
    form_class = RegUsersForm
    template_name = 'login_singup_page/reg_page.html'

    def post(self, request):
        res_form = RegUsersForm(request.POST)
        if res_form.is_valid():
            send_aprove_mail(request.POST["email"], request.POST["username"], request.POST["first_name"],
                             request.POST["last_name"])
            create_avatar_link(request.POST["username"])
            create_user_crypto_bills(request.POST["username"])
            create_user_usd_bill(request.POST["username"])
            request.user.username = request.POST["username"]

        return super(RegistrationView, self).post(request)


class CustLoginView(LoginView):
    form_class = LogUsersForm
    template_name = 'login_singup_page/login_page.html'

    def get_success_url(self):
        return '/./user/'

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        if not verifiction_check(username):
            return redirect("/./login/")

        return super(CustLoginView, self).post(self, request, *args, **kwargs)
