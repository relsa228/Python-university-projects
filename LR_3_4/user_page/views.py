from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import UserUsdAcc, UserCryptoAcc
from home_page.models import BTC, ETH, ZEC, DASH, LTC, XRP

from .forms import RedactForm, UsdDepositForm, CryptoForm
from .utils import get_wallets, get_profit


class RedactUserView(CreateView):
    success_url = ''
    form_class = RedactForm
    template_name = 'user_page/profile.html'


def deposit(request):
    if request.method == "POST":
        result = UsdDepositForm(request.POST)
        user_acc = UserUsdAcc.objects.get(username=request.user.username)
        user_acc.usd_count = float(user_acc.usd_count) + float(result.data["usd_count"])
        user_acc.save()
    data = {
        "usd_deposit_form": UsdDepositForm
    }
    return render(request, 'user_page/deposit.html', data)


def buy(request):
    if request.method == "POST":
        result = CryptoForm(request.POST)
        user_acc = UserCryptoAcc.objects.get(username=request.user.username, crypto_ticker=result.data["crypto_ticker"])
        user_usd_acc = UserUsdAcc.objects.get(username=request.user.username)
        current_price = 0
        match result.data["crypto_ticker"]:
            case "BTC":
                current_price = BTC.objects.last().current_buy_price
            case "ETH":
                current_price = ETH.objects.last().current_buy_price
            case "LTC":
                current_price = LTC.objects.last().current_buy_price
            case "XRP":
                current_price = XRP.objects.last().current_buy_price
            case "ZEC":
                current_price = ZEC.objects.last().current_buy_price
            case "DASH":
                current_price = DASH.objects.last().current_buy_price
        if float(current_price) * float(result.data["token_count"]) <= float(user_usd_acc.usd_count):
            user_acc.token_count = float(user_acc.token_count) + float(result.data["token_count"])
            user_acc.usd_in = float(user_acc.usd_in) + float(current_price) * float(result.data["token_count"])
            user_usd_acc.usd_count = float(user_usd_acc.usd_count) - (float(current_price) * float(result.data["token_count"]))
            user_acc.save()
            user_usd_acc.save()
    data = {
        "crypto_buy_form": CryptoForm
    }
    return render(request, 'user_page/crypto_buy.html', data)


def sell(request):
    if request.method == "POST":
        result = CryptoForm(request.POST)
        user_acc = UserCryptoAcc.objects.get(username=request.user.username, crypto_ticker=result.data["crypto_ticker"])
        user_usd_acc = UserUsdAcc.objects.get(username=request.user.username)
        current_price = 0
        match result.data["crypto_ticker"]:
            case "BTC":
                current_price = BTC.objects.last().current_buy_price
            case "ETH":
                current_price = ETH.objects.last().current_buy_price
            case "LTC":
                current_price = LTC.objects.last().current_buy_price
            case "XRP":
                current_price = XRP.objects.last().current_buy_price
            case "ZEC":
                current_price = ZEC.objects.last().current_buy_price
            case "DASH":
                current_price = DASH.objects.last().current_buy_price
        if float(user_acc.token_count) >= float(result.data["token_count"]):
            user_acc.token_count = float(user_acc.token_count) - float(result.data["token_count"])
            user_acc.usd_in = float(user_acc.usd_in) - float(current_price) * float(result.data["token_count"])
            user_usd_acc.usd_count = float(user_usd_acc.usd_count) + (float(current_price) * float(result.data["token_count"]))
            user_acc.save()
            user_usd_acc.save()
    data = {
        "crypto_buy_form": CryptoForm
    }
    return render(request, 'user_page/crypto_sell.html', data)


def wallet(request):
    crypto_wallets, usd_wallet = get_wallets(request.user.username)
    crypto_profit = get_profit(crypto_wallets)

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

        'usd_acc': usd_wallet
    }
    return render(request, 'user_page/wallet.html', data)


def profile(request):
    return render(request, 'user_page/profile.html')


def edit(request):
    return render(request, 'user_page/redact_profile.html')
