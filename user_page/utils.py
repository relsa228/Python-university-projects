import threading

from django.contrib.auth.models import User

from home_page.models import BTC, ETH, XRP, ZEC, LTC, DASH
from .models import UserCryptoAcc, UserUsdAcc, UsersAvatars


class AvatarThread(threading.Thread):
    def __init__(self, username, link):
        threading.Thread.__init__(self)
        self.link = link
        self.username = username

    def run(self) -> None:
        upload_avatar(self.username, self.link)


class RedactThread(threading.Thread):
    def __init__(self, username, first_name, last_name, email):
        threading.Thread.__init__(self)
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def run(self) -> None:
        edit_profile(self.username, self.first_name, self.last_name, self.email)


def get_wallets(username):
    current_btc_price = BTC.objects.last().current_sell_price
    current_eth_price = ETH.objects.last().current_sell_price
    current_xrp_price = XRP.objects.last().current_sell_price
    current_zec_price = ZEC.objects.last().current_sell_price
    current_ltc_price = LTC.objects.last().current_sell_price
    current_dash_price = DASH.objects.last().current_sell_price

    crypto_wallets = {}
    get_data = UserCryptoAcc.objects.filter(username=username)
    for acc in get_data:
        match acc.crypto_ticker:
            case "BTC":
                acc.usd_count = float(acc.token_count) * float(current_btc_price)
            case "ETH":
                acc.usd_count = float(acc.token_count) * float(current_eth_price)
            case "XRP":
                acc.usd_count = float(acc.token_count) * float(current_xrp_price)
            case "LTC":
                acc.usd_count = float(acc.token_count) * float(current_ltc_price)
            case "DASH":
                acc.usd_count = float(acc.token_count) * float(current_dash_price)
            case "ZEC":
                acc.usd_count = float(acc.token_count) * float(current_zec_price)

        crypto_wallets[acc.crypto_ticker] = acc

    usd_wallet = UserUsdAcc.objects.filter(username=username)
    usd_res = 0
    for wal in usd_wallet:
        usd_res = wal.usd_count

    return crypto_wallets, usd_res


def get_profit(crypto_wallets):
    tikers = ["BTC", "ETH", "LTC", "XRP", "ZEC", "DASH"]
    result_dict = {}

    for ticker in tikers:
        try:
            result = float(crypto_wallets[ticker].usd_count) / float(crypto_wallets[ticker].usd_in) - 1
            result_dict[ticker] = round(result, 3)
        except ZeroDivisionError as e:
            result_dict[ticker] = 0

    return result_dict


def buy_sell_helper(username, result):
    user_acc = UserCryptoAcc.objects.get(username=username, crypto_ticker=result.data["crypto_ticker"])
    user_usd_acc = UserUsdAcc.objects.get(username=username)
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

    return user_acc, user_usd_acc, current_price


def buy_crypto(username, result) -> bool:
    if float(result.data["token_count"]) <= 0:
        return False
    user_acc, user_usd_acc, current_price = buy_sell_helper(username, result)
    if float(current_price) * float(result.data["token_count"]) <= float(user_usd_acc.usd_count):
        user_acc.token_count = float(user_acc.token_count) + float(result.data["token_count"])
        user_acc.usd_in = float(user_acc.usd_in) + float(current_price) * float(result.data["token_count"])
        user_usd_acc.usd_count = float(user_usd_acc.usd_count) - (
                    float(current_price) * float(result.data["token_count"]))
        user_acc.save()
        user_usd_acc.save()
        return True

    return False


def sell_crypto(username, result) -> bool:
    if float(result.data["token_count"]) <= 0:
        return False
    user_acc, user_usd_acc, current_price = buy_sell_helper(username, result)
    if float(user_acc.token_count) >= float(result.data["token_count"]):
        user_acc.token_count = float(user_acc.token_count) - float(result.data["token_count"])
        user_acc.usd_in = float(user_acc.usd_in) - float(current_price) * float(result.data["token_count"])
        user_usd_acc.usd_count = float(user_usd_acc.usd_count) + (
                float(current_price) * float(result.data["token_count"]))
        user_acc.save()
        user_usd_acc.save()
        return True

    return False


def edit_profile(username, first_name, last_name, email):
    user = User.objects.get(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()


def upload_avatar(username, imgur_link):
    user_acc = UsersAvatars.objects.get(username=username)
    user_acc.imgur_link = imgur_link
    user_acc.save()


def get_avatar_link(username):
    user_acc = UsersAvatars.objects.get(username=username)
    return user_acc.imgur_link

