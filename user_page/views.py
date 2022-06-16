from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .forms import RedactForm, UsdDepositForm, CryptoForm
from .models import UserUsdAcc
from .utils import get_wallets, get_profit, buy_crypto, sell_crypto, get_avatar_link, RedactThread, AvatarThread


class RedactUserView(LoginRequiredMixin, CreateView):
    login_url = '/./login/'
    success_url = '/./user/'
    form_class = RedactForm
    template_name = 'user_page/redact_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imgur_link'] = get_avatar_link(self.request.user.username)
        return context

    def get_success_url(self):
        return '/./user/'

    def post(self, request, **kwargs):
        result = RedactForm(request.POST)
        avatar_pic = request.POST["aprove_btn"]
        if avatar_pic != "":
            upload_avatar = AvatarThread(request.user.username, avatar_pic)
            upload_avatar.run()
        if result.is_valid():
            username, first_name, last_name, email = request.user.username, result.data["first_name"], \
                                                     result.data["last_name"], result.data["email"]
            redaction = RedactThread(username, first_name, last_name, email)
            redaction.run()
            return redirect("/./user/")

        return super(RedactUserView, self).post(request)


class DepositView(LoginRequiredMixin, CreateView):
    login_url = '/./login/'
    form_class = UsdDepositForm
    template_name = 'user_page/deposit.html'
    success_url = '/./user/deposit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imgur_link'] = get_avatar_link(self.request.user.username)
        return context

    def post(self, request, **kwargs):
        result = UsdDepositForm(request.POST)
        if float(result.data["usd_count"]) > 0:
            user_acc = UserUsdAcc.objects.get(username=request.user.username)
            user_acc.usd_count = float(user_acc.usd_count) + float(result.data["usd_count"])
            user_acc.save()

        return super(DepositView, self).post(request)


@login_required(login_url='/./login/')
def buy(request):
    error_msg = ""
    imgur_link = get_avatar_link(request.user.username)

    if request.method == "POST":
        result = CryptoForm(request.POST)
        username = request.user.username
        if buy_crypto(username, result):
            error_msg = ""
        else:
            error_msg = "Операция не может быть проведена"
    data = {
        "crypto_buy_form": CryptoForm,
        "error_msg": error_msg,
        "imgur_link": imgur_link
    }
    return render(request, 'user_page/crypto_buy.html', data)


@login_required(login_url='/./login/')
def sell(request):
    error_msg = ""
    imgur_link = get_avatar_link(request.user.username)

    if request.method == "POST":
        result = CryptoForm(request.POST)
        username = request.user.username
        if sell_crypto(username, result):
            error_msg = ""
        else:
            error_msg = "Операция не может быть проведена"
    data = {
        "crypto_sell_form": CryptoForm,
        "error_msg": error_msg,
        "imgur_link": imgur_link
    }
    return render(request, 'user_page/crypto_sell.html', data)


class ProfileView(LoginRequiredMixin, CreateView):
    login_url = '/./login/'
    form_class = RedactForm
    template_name = 'user_page/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imgur_link'] = get_avatar_link(self.request.user.username)
        return context


class WalletView(LoginRequiredMixin, CreateView):
    login_url = '/./login/'
    form_class = RedactForm
    template_name = 'user_page/wallet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crypto_wallets, usd_wallet = get_wallets(self.request.user.username)
        crypto_profit = get_profit(crypto_wallets)
        imgur_link = get_avatar_link(self.request.user.username)
        context['btc_acc_count'] = crypto_wallets["BTC"].token_count
        context['btc_acc_price'] = crypto_wallets["BTC"].usd_count
        context['btc_profit'] = crypto_profit["BTC"]

        context['eth_acc_count'] = crypto_wallets["ETH"].token_count
        context['eth_acc_price'] = crypto_wallets["ETH"].usd_count
        context['eth_profit'] = crypto_profit["ETH"]

        context['xrp_acc_count'] = crypto_wallets["XRP"].token_count
        context['xrp_acc_price'] = crypto_wallets["XRP"].usd_count
        context['xrp_profit'] = crypto_profit["XRP"]

        context['zec_acc_count'] = crypto_wallets["ZEC"].token_count
        context['zec_acc_price'] = crypto_wallets["ZEC"].usd_count
        context['zec_profit'] = crypto_profit["ZEC"]

        context['ltc_acc_count'] = crypto_wallets["LTC"].token_count
        context['ltc_acc_price'] = crypto_wallets["LTC"].usd_count
        context['ltc_profit'] = crypto_profit["LTC"]

        context['dash_acc_count'] = crypto_wallets["DASH"].token_count
        context['dash_acc_price'] = crypto_wallets["DASH"].usd_count
        context['dash_profit'] = crypto_profit["DASH"]

        context['usd_acc'] = usd_wallet

        context['imgur_link'] = imgur_link
        return context
