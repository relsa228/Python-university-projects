from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .forms import RedactForm, UsdDepositForm, CryptoForm
from .models import UserUsdAcc
from .utils import get_wallets, get_profit, buy_crypto, sell_crypto, edit_profile, upload_avatar, get_avatar_link


class RedactUserView(CreateView):
    success_url = '/./user/'
    form_class = RedactForm
    template_name = 'user_page/redact_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imgur_link'] = get_avatar_link(self.request.user.username)

        return context

    def get_success_url(self):
        return '/./user/'

    def post(self, request):
        result = RedactForm(request.POST)
        avatar_pic = request.POST["aprove_btn"]
        upload_avatar(request.user.username, avatar_pic)
        if result.is_valid():
            username, f_name, s_name, email = request.user.username, result.data["first_name"], result.data[
                "last_name"], \
                                              result.data["email"]
            edit_profile(username, f_name, s_name, email)
            return redirect("/./user/")

        return super(RedactUserView, self).post(request)


class DepositView(CreateView):
    form_class = UsdDepositForm
    template_name = 'user_page/deposit.html'
    success_url = '/./user/deposit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imgur_link'] = get_avatar_link(self.request.user.username)
        return context

    def post(self, request):
        result = UsdDepositForm(request.POST)
        if float(result.data["usd_count"]) > 0:
            user_acc = UserUsdAcc.objects.get(username=request.user.username)
            user_acc.usd_count = float(user_acc.usd_count) + float(result.data["usd_count"])
            user_acc.save()

        return super(DepositView, self).post(request)


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


def wallet(request):
    crypto_wallets, usd_wallet = get_wallets(request.user.username)
    crypto_profit = get_profit(crypto_wallets)
    imgur_link = get_avatar_link(request.user.username)

    data = {
        'btc_acc_count': crypto_wallets["BTC"].token_count,
        'btc_acc_price': crypto_wallets["BTC"].usd_count,
        'btc_profit': crypto_profit["BTC"],

        'eth_acc_count': crypto_wallets["ETH"].token_count,
        'eth_acc_price': crypto_wallets["ETH"].usd_count,
        'eth_profit': crypto_profit["ETH"],

        'xrp_acc_count': crypto_wallets["XRP"].token_count,
        'xrp_acc_price': crypto_wallets["XRP"].usd_count,
        'xrp_profit': crypto_profit["XRP"],

        'zec_acc_count': crypto_wallets["ZEC"].token_count,
        'zec_acc_price': crypto_wallets["ZEC"].usd_count,
        'zec_profit': crypto_profit["ZEC"],

        'ltc_acc_count': crypto_wallets["LTC"].token_count,
        'ltc_acc_price': crypto_wallets["LTC"].usd_count,
        'ltc_profit': crypto_profit["LTC"],

        'dash_acc_count': crypto_wallets["DASH"].token_count,
        'dash_acc_price': crypto_wallets["DASH"].usd_count,
        'dash_profit': crypto_profit["DASH"],

        'usd_acc': usd_wallet,

        'imgur_link': imgur_link
    }
    return render(request, 'user_page/wallet.html', data)


class ProfileView(CreateView):
    form_class = RedactForm
    template_name = 'user_page/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imgur_link'] = get_avatar_link(self.request.user.username)
        return context


class WalletView(CreateView):
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
