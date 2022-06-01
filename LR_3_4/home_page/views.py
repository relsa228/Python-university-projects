from .models import BTC, ETH, LTC, ZEC, DASH, XRP
from django.shortcuts import render, redirect
from django.contrib.auth import logout

bitcoin_quore = BTC.objects.all()[BTC.objects.count()-7:]


def index(request):
    list_of_btc_prices = []
    for el in bitcoin_quore:
        list_of_btc_prices.append(el.avg_price)

    list_of_btc_date = []
    for el in bitcoin_quore:
        list_of_btc_date.append(str(el.date)[5:-9])

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
    }
    return render(request, 'home_page/btc_page.html', data)


def eth_overview(request):
    ether_quore = ETH.objects.all()[:7]

    list_of_eth_prices = []
    for el in ether_quore:
        list_of_eth_prices.append(el.avg_price)

    list_of_eth_date = []
    for el in ether_quore:
        list_of_eth_date.append(str(el.date)[5:-9])

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
    }
    return render(request, 'home_page/btc_page.html', data)


def ltc_overview(request):
    bitcoin_quore = BTC.objects.all()[:7]

    list_of_btc_prices = []
    for el in bitcoin_quore:
        list_of_btc_prices.append(el.avg_price)

    list_of_btc_date = []
    for el in bitcoin_quore:
        list_of_btc_date.append(str(el.date)[5:-9])

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
    }
    return render(request, 'home_page/btc_page.html', data)


def xrp_overview(request):
    bitcoin_quore = BTC.objects.all()[:7]

    list_of_btc_prices = []
    for el in bitcoin_quore:
        list_of_btc_prices.append(el.avg_price)

    list_of_btc_date = []
    for el in bitcoin_quore:
        list_of_btc_date.append(str(el.date)[5:-9])

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
    }
    return render(request, 'home_page/btc_page.html', data)


def dash_overview(request):
    bitcoin_quore = BTC.objects.all()[:7]

    list_of_btc_prices = []
    for el in bitcoin_quore:
        list_of_btc_prices.append(el.avg_price)

    list_of_btc_date = []
    for el in bitcoin_quore:
        list_of_btc_date.append(str(el.date)[5:-9])

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
    }
    return render(request, 'home_page/btc_page.html', data)


def zec_overview(request):
    bitcoin_quore = BTC.objects.all()[:7]

    list_of_btc_prices = []
    for el in bitcoin_quore:
        list_of_btc_prices.append(el.avg_price)

    list_of_btc_date = []
    for el in bitcoin_quore:
        list_of_btc_date.append(str(el.date)[5:-9])

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
    }
    return render(request, 'home_page/btc_page.html', data)


def logout_user(request):
    logout(request)
    return redirect('/./')
