from .models import UserCryptoAcc, UserUsdAcc
from home_page.models import BTC, ETH, XRP, ZEC, LTC, DASH


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
            result_dict[ticker] = float(crypto_wallets[ticker].usd_count) / float(crypto_wallets[ticker].usd_in) - 1
        except ZeroDivisionError as e:
            result_dict[ticker] = 0

    return result_dict
