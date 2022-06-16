from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from .forms import RegUsersForm, LogUsersForm, VerificationForm
from .utils import verificate_user, verifiction_check, EmailThread, CreateUserPropertiesThread


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


class RegistrationView(CreateView):
    success_url = 'verificate_email/'
    form_class = RegUsersForm
    template_name = 'login_singup_page/reg_page.html'

    def post(self, request, **kwargs):
        res_form = RegUsersForm(request.POST)
        if res_form.is_valid():
            mail = EmailThread(request.POST["email"], request.POST["username"], request.POST["first_name"],
                               request.POST["last_name"])
            mail.run()

            create_prop = CreateUserPropertiesThread(request.POST["username"])
            create_prop.run()

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


def emal_aprove(request):
    return render(request, 'login_singup_page/email_aprove_page.html')
