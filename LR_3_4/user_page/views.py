from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import RedactForm
from .utils import get_wallets


class RedactUserView(CreateView):
    success_url = ''
    form_class = RedactForm
    template_name = 'user_page/profile.html'


def deposit(request):
    return render(request, 'user_page/deposit.html')


def wallet(request):
    crypto_wallets, usd_wallet = get_wallets(request.user.username)
    data = {
        'btc_acc_count': crypto_wallets["BTC"].token_count,
        'btc_acc_price': crypto_wallets["BTC"].usd_count,

        'eth_acc_count': crypto_wallets["ETH"].token_count,
        'eth_acc_price': crypto_wallets["ETH"].usd_count,

        'xrp_acc_count': crypto_wallets["XRP"].token_count,
        'xrp_acc_price': crypto_wallets["XRP"].usd_count,

        'zec_acc_count': crypto_wallets["ZEC"].token_count,
        'zec_acc_price': crypto_wallets["ZEC"].usd_count,

        'ltc_acc_count': crypto_wallets["LTC"].token_count,
        'ltc_acc_price': crypto_wallets["LTC"].usd_count,

        'dash_acc_count': crypto_wallets["DASH"].token_count,
        'dash_acc_price': crypto_wallets["DASH"].usd_count,

        'usd_acc': usd_wallet
    }
    return render(request, 'user_page/wallet.html', data)


def profile(request):
    return render(request, 'user_page/profile.html')


def edit(request):
    return render(request, 'user_page/redact_profile.html')
