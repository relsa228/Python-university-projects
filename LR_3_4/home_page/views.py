from .models import BTC, ETH, LTC, ZEC, DASH, XRP
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .utils import get_current_data

green_color = "#228B22"
red_color = "#8B0000"


def index(request):
    bitcoin_quore, ether_quore, litecoin_quore, ripple_quore, zcash_quore, dash_quore = get_current_data()

    list_of_btc_prices = []
    for el in bitcoin_quore:
        list_of_btc_prices.append(el.current_sell_price)

    list_of_btc_date = []
    for el in bitcoin_quore:
        list_of_btc_date.append(str(el.date)[5:-16])

    if list_of_btc_prices[5] < list_of_btc_prices[6]:
        current_color = green_color
    else:
        current_color = red_color

    data = {
        'btc_price_0': list_of_btc_prices[0],
        'btc_price_1': list_of_btc_prices[1],
        'btc_price_2': list_of_btc_prices[2],
        'btc_price_3': list_of_btc_prices[3],
        'btc_price_4': list_of_btc_prices[4],
        'btc_price_5': list_of_btc_prices[5],
        'btc_price_6': list_of_btc_prices[6],

        'btc_date_0': list_of_btc_date[0],
        'btc_date_1': list_of_btc_date[1],
        'btc_date_2': list_of_btc_date[2],
        'btc_date_3': list_of_btc_date[3],
        'btc_date_4': list_of_btc_date[4],
        'btc_date_5': list_of_btc_date[5],
        'btc_date_6': list_of_btc_date[6],

        'btc_buy': bitcoin_quore[6].current_buy_price,
        'btc_sell': bitcoin_quore[6].current_sell_price,
        'btc_date': str(bitcoin_quore[6].date)[5:-16],
        'btc_avg': bitcoin_quore[6].avg_price,

        'eth_buy': ether_quore[6].current_buy_price,
        'eth_sell': ether_quore[6].current_sell_price,
        'eth_date': str(ether_quore[6].date)[5:-16],
        'eth_avg': ether_quore[6].avg_price,

        'ltc_buy': litecoin_quore[6].current_buy_price,
        'ltc_sell': litecoin_quore[6].current_sell_price,
        'ltc_date': str(litecoin_quore[6].date)[5:-16],
        'ltc_avg': litecoin_quore[6].avg_price,

        'xrp_buy': ripple_quore[6].current_buy_price,
        'xrp_sell': ripple_quore[6].current_sell_price,
        'xrp_date': str(ripple_quore[6].date)[5:-16],
        'xrp_avg': ripple_quore[6].avg_price,

        'zec_buy': zcash_quore[6].current_buy_price,
        'zec_sell': zcash_quore[6].current_sell_price,
        'zec_date': str(zcash_quore[6].date)[5:-16],
        'zec_avg': zcash_quore[6].avg_price,

        'dash_buy': dash_quore[6].current_buy_price,
        'dash_sell': dash_quore[6].current_sell_price,
        'dash_date': str(dash_quore[6].date)[5:-16],
        'dash_avg': dash_quore[6].avg_price,

        'current_color': current_color
    }
    return render(request, 'home_page/btc_page.html', data)


def eth_overview(request):
    bitcoin_quore, ether_quore, litecoin_quore, ripple_quore, zcash_quore, dash_quore = get_current_data()

    list_of_eth_prices = []
    for el in ether_quore:
        list_of_eth_prices.append(el.avg_price)

    list_of_eth_date = []
    for el in ether_quore:
        list_of_eth_date.append(str(el.date)[5:-16])

    if list_of_eth_prices[5] < list_of_eth_prices[6]:
        current_color = green_color
    else:
        current_color = red_color

    data = {
        'eth_price_0': list_of_eth_prices[0],
        'eth_price_1': list_of_eth_prices[1],
        'eth_price_2': list_of_eth_prices[2],
        'eth_price_3': list_of_eth_prices[3],
        'eth_price_4': list_of_eth_prices[4],
        'eth_price_5': list_of_eth_prices[5],
        'eth_price_6': list_of_eth_prices[6],

        'eth_date_0': list_of_eth_date[0],
        'eth_date_1': list_of_eth_date[1],
        'eth_date_2': list_of_eth_date[2],
        'eth_date_3': list_of_eth_date[3],
        'eth_date_4': list_of_eth_date[4],
        'eth_date_5': list_of_eth_date[5],
        'eth_date_6': list_of_eth_date[6],

        'btc_buy': bitcoin_quore[6].current_buy_price,
        'btc_sell': bitcoin_quore[6].current_sell_price,
        'btc_date': str(bitcoin_quore[6].date)[5:-16],
        'btc_avg': bitcoin_quore[6].avg_price,

        'eth_buy': ether_quore[6].current_buy_price,
        'eth_sell': ether_quore[6].current_sell_price,
        'eth_date': str(ether_quore[6].date)[5:-16],
        'eth_avg': ether_quore[6].avg_price,

        'ltc_buy': litecoin_quore[6].current_buy_price,
        'ltc_sell': litecoin_quore[6].current_sell_price,
        'ltc_date': str(litecoin_quore[6].date)[5:-16],
        'ltc_avg': litecoin_quore[6].avg_price,

        'xrp_buy': ripple_quore[6].current_buy_price,
        'xrp_sell': ripple_quore[6].current_sell_price,
        'xrp_date': str(ripple_quore[6].date)[5:-16],
        'xrp_avg': ripple_quore[6].avg_price,

        'zec_buy': zcash_quore[6].current_buy_price,
        'zec_sell': zcash_quore[6].current_sell_price,
        'zec_date': str(zcash_quore[6].date)[5:-16],
        'zec_avg': zcash_quore[6].avg_price,

        'dash_buy': dash_quore[6].current_buy_price,
        'dash_sell': dash_quore[6].current_sell_price,
        'dash_date': str(dash_quore[6].date)[5:-16],
        'dash_avg': dash_quore[6].avg_price,

        'current_color': current_color
    }
    return render(request, 'home_page/eth_page.html', data)


def ltc_overview(request):
    bitcoin_quore, ether_quore, litecoin_quore, ripple_quore, zcash_quore, dash_quore = get_current_data()

    list_of_ltc_prices = []
    for el in litecoin_quore:
        list_of_ltc_prices.append(el.avg_price)

    list_of_ltc_date = []
    for el in litecoin_quore:
        list_of_ltc_date.append(str(el.date)[5:-16])

    if list_of_ltc_prices[5] < list_of_ltc_prices[6]:
        current_color = green_color
    else:
        current_color = red_color

    data = {
        'ltc_price_0': list_of_ltc_prices[0],
        'ltc_price_1': list_of_ltc_prices[1],
        'ltc_price_2': list_of_ltc_prices[2],
        'ltc_price_3': list_of_ltc_prices[3],
        'ltc_price_4': list_of_ltc_prices[4],
        'ltc_price_5': list_of_ltc_prices[5],
        'ltc_price_6': list_of_ltc_prices[6],

        'ltc_date_0': list_of_ltc_date[0],
        'ltc_date_1': list_of_ltc_date[1],
        'ltc_date_2': list_of_ltc_date[2],
        'ltc_date_3': list_of_ltc_date[3],
        'ltc_date_4': list_of_ltc_date[4],
        'ltc_date_5': list_of_ltc_date[5],
        'ltc_date_6': list_of_ltc_date[6],

        'btc_buy': bitcoin_quore[6].current_buy_price,
        'btc_sell': bitcoin_quore[6].current_sell_price,
        'btc_date': str(bitcoin_quore[6].date)[5:-16],
        'btc_avg': bitcoin_quore[6].avg_price,

        'eth_buy': ether_quore[6].current_buy_price,
        'eth_sell': ether_quore[6].current_sell_price,
        'eth_date': str(ether_quore[6].date)[5:-16],
        'eth_avg': ether_quore[6].avg_price,

        'ltc_buy': litecoin_quore[6].current_buy_price,
        'ltc_sell': litecoin_quore[6].current_sell_price,
        'ltc_date': str(litecoin_quore[6].date)[5:-16],
        'ltc_avg': litecoin_quore[6].avg_price,

        'xrp_buy': ripple_quore[6].current_buy_price,
        'xrp_sell': ripple_quore[6].current_sell_price,
        'xrp_date': str(ripple_quore[6].date)[5:-16],
        'xrp_avg': ripple_quore[6].avg_price,

        'zec_buy': zcash_quore[6].current_buy_price,
        'zec_sell': zcash_quore[6].current_sell_price,
        'zec_date': str(zcash_quore[6].date)[5:-16],
        'zec_avg': zcash_quore[6].avg_price,

        'dash_buy': dash_quore[6].current_buy_price,
        'dash_sell': dash_quore[6].current_sell_price,
        'dash_date': str(dash_quore[6].date)[5:-16],
        'dash_avg': dash_quore[6].avg_price,

        'current_color': current_color
    }
    return render(request, 'home_page/ltc_page.html', data)


def xrp_overview(request):
    bitcoin_quore, ether_quore, litecoin_quore, ripple_quore, zcash_quore, dash_quore = get_current_data()

    list_of_xrp_prices = []
    for el in ripple_quore:
        list_of_xrp_prices.append(el.avg_price)

    list_of_xrp_date = []
    for el in ripple_quore:
        list_of_xrp_date.append(str(el.date)[5:-16])

    if list_of_xrp_prices[5] < list_of_xrp_prices[6]:
        current_color = green_color
    else:
        current_color = red_color

    data = {
        'xrp_price_0': list_of_xrp_prices[0],
        'xrp_price_1': list_of_xrp_prices[1],
        'xrp_price_2': list_of_xrp_prices[2],
        'xrp_price_3': list_of_xrp_prices[3],
        'xrp_price_4': list_of_xrp_prices[4],
        'xrp_price_5': list_of_xrp_prices[5],
        'xrp_price_6': list_of_xrp_prices[6],

        'xrp_date_0': list_of_xrp_date[0],
        'xrp_date_1': list_of_xrp_date[1],
        'xrp_date_2': list_of_xrp_date[2],
        'xrp_date_3': list_of_xrp_date[3],
        'xrp_date_4': list_of_xrp_date[4],
        'xrp_date_5': list_of_xrp_date[5],
        'xrp_date_6': list_of_xrp_date[6],

        'btc_buy': bitcoin_quore[6].current_buy_price,
        'btc_sell': bitcoin_quore[6].current_sell_price,
        'btc_date': str(bitcoin_quore[6].date)[5:-16],
        'btc_avg': bitcoin_quore[6].avg_price,

        'eth_buy': ether_quore[6].current_buy_price,
        'eth_sell': ether_quore[6].current_sell_price,
        'eth_date': str(ether_quore[6].date)[5:-16],
        'eth_avg': ether_quore[6].avg_price,

        'ltc_buy': litecoin_quore[6].current_buy_price,
        'ltc_sell': litecoin_quore[6].current_sell_price,
        'ltc_date': str(litecoin_quore[6].date)[5:-16],
        'ltc_avg': litecoin_quore[6].avg_price,

        'xrp_buy': ripple_quore[6].current_buy_price,
        'xrp_sell': ripple_quore[6].current_sell_price,
        'xrp_date': str(ripple_quore[6].date)[5:-16],
        'xrp_avg': ripple_quore[6].avg_price,

        'zec_buy': zcash_quore[6].current_buy_price,
        'zec_sell': zcash_quore[6].current_sell_price,
        'zec_date': str(zcash_quore[6].date)[5:-16],
        'zec_avg': zcash_quore[6].avg_price,

        'dash_buy': dash_quore[6].current_buy_price,
        'dash_sell': dash_quore[6].current_sell_price,
        'dash_date': str(dash_quore[6].date)[5:-16],
        'dash_avg': dash_quore[6].avg_price,

        'current_color': current_color
    }
    return render(request, 'home_page/xrp_page.html', data)


def dash_overview(request):
    bitcoin_quore, ether_quore, litecoin_quore, ripple_quore, zcash_quore, dash_quore = get_current_data()

    list_of_dash_prices = []
    for el in dash_quore:
        list_of_dash_prices.append(el.avg_price)

    list_of_dash_date = []
    for el in dash_quore:
        list_of_dash_date.append(str(el.date)[5:-16])

    if list_of_dash_prices[5] < list_of_dash_prices[6]:
        current_color = green_color
    else:
        current_color = red_color

    data = {
        'dash_price_0': list_of_dash_prices[0],
        'dash_price_1': list_of_dash_prices[1],
        'dash_price_2': list_of_dash_prices[2],
        'dash_price_3': list_of_dash_prices[3],
        'dash_price_4': list_of_dash_prices[4],
        'dash_price_5': list_of_dash_prices[5],
        'dash_price_6': list_of_dash_prices[6],

        'dash_date_0': list_of_dash_date[0],
        'dash_date_1': list_of_dash_date[1],
        'dash_date_2': list_of_dash_date[2],
        'dash_date_3': list_of_dash_date[3],
        'dash_date_4': list_of_dash_date[4],
        'dash_date_5': list_of_dash_date[5],
        'dash_date_6': list_of_dash_date[6],

        'btc_buy': bitcoin_quore[6].current_buy_price,
        'btc_sell': bitcoin_quore[6].current_sell_price,
        'btc_date': str(bitcoin_quore[6].date)[5:-16],
        'btc_avg': bitcoin_quore[6].avg_price,

        'eth_buy': ether_quore[6].current_buy_price,
        'eth_sell': ether_quore[6].current_sell_price,
        'eth_date': str(ether_quore[6].date)[5:-16],
        'eth_avg': ether_quore[6].avg_price,

        'ltc_buy': litecoin_quore[6].current_buy_price,
        'ltc_sell': litecoin_quore[6].current_sell_price,
        'ltc_date': str(litecoin_quore[6].date)[5:-16],
        'ltc_avg': litecoin_quore[6].avg_price,

        'xrp_buy': ripple_quore[6].current_buy_price,
        'xrp_sell': ripple_quore[6].current_sell_price,
        'xrp_date': str(ripple_quore[6].date)[5:-16],
        'xrp_avg': ripple_quore[6].avg_price,

        'zec_buy': zcash_quore[6].current_buy_price,
        'zec_sell': zcash_quore[6].current_sell_price,
        'zec_date': str(zcash_quore[6].date)[5:-16],
        'zec_avg': zcash_quore[6].avg_price,

        'dash_buy': dash_quore[6].current_buy_price,
        'dash_sell': dash_quore[6].current_sell_price,
        'dash_date': str(dash_quore[6].date)[5:-16],
        'dash_avg': dash_quore[6].avg_price,

        'current_color': current_color
    }
    return render(request, 'home_page/dash_page.html', data)


def zec_overview(request):
    bitcoin_quore, ether_quore, litecoin_quore, ripple_quore, zcash_quore, dash_quore = get_current_data()

    list_of_zec_prices = []
    for el in zcash_quore:
        list_of_zec_prices.append(el.avg_price)

    list_of_zec_date = []
    for el in zcash_quore:
        list_of_zec_date.append(str(el.date)[5:-16])

    if list_of_zec_prices[5] < list_of_zec_prices[6]:
        current_color = green_color
    else:
        current_color = red_color

    data = {
        'zec_price_0': list_of_zec_prices[0],
        'zec_price_1': list_of_zec_prices[1],
        'zec_price_2': list_of_zec_prices[2],
        'zec_price_3': list_of_zec_prices[3],
        'zec_price_4': list_of_zec_prices[4],
        'zec_price_5': list_of_zec_prices[5],
        'zec_price_6': list_of_zec_prices[6],

        'zec_date_0': list_of_zec_date[0],
        'zec_date_1': list_of_zec_date[1],
        'zec_date_2': list_of_zec_date[2],
        'zec_date_3': list_of_zec_date[3],
        'zec_date_4': list_of_zec_date[4],
        'zec_date_5': list_of_zec_date[5],
        'zec_date_6': list_of_zec_date[6],

        'btc_buy': bitcoin_quore[6].current_buy_price,
        'btc_sell': bitcoin_quore[6].current_sell_price,
        'btc_date': str(bitcoin_quore[6].date)[5:-16],
        'btc_avg': bitcoin_quore[6].avg_price,

        'eth_buy': ether_quore[6].current_buy_price,
        'eth_sell': ether_quore[6].current_sell_price,
        'eth_date': str(ether_quore[6].date)[5:-16],
        'eth_avg': ether_quore[6].avg_price,

        'ltc_buy': litecoin_quore[6].current_buy_price,
        'ltc_sell': litecoin_quore[6].current_sell_price,
        'ltc_date': str(litecoin_quore[6].date)[5:-16],
        'ltc_avg': litecoin_quore[6].avg_price,

        'xrp_buy': ripple_quore[6].current_buy_price,
        'xrp_sell': ripple_quore[6].current_sell_price,
        'xrp_date': str(ripple_quore[6].date)[5:-16],
        'xrp_avg': ripple_quore[6].avg_price,

        'zec_buy': zcash_quore[6].current_buy_price,
        'zec_sell': zcash_quore[6].current_sell_price,
        'zec_date': str(zcash_quore[6].date)[5:-16],
        'zec_avg': zcash_quore[6].avg_price,

        'dash_buy': dash_quore[6].current_buy_price,
        'dash_sell': dash_quore[6].current_sell_price,
        'dash_date': str(dash_quore[6].date)[5:-16],
        'dash_avg': dash_quore[6].avg_price,

        'current_color': current_color
    }
    return render(request, 'home_page/zec_page.html', data)


def logout_user(request):
    logout(request)
    return redirect('/./')
