from .models import BTC, ETH, LTC, ZEC, DASH, XRP


def get_current_data():
    bitcoin_quore = BTC.objects.all()[BTC.objects.count() - 7:]
    ether_quore = ETH.objects.all()[ETH.objects.count() - 7:]
    litecoin_quore = LTC.objects.all()[LTC.objects.count() - 7:]
    ripple_quore = XRP.objects.all()[XRP.objects.count() - 7:]
    zcash_quore = ZEC.objects.all()[ZEC.objects.count() - 7:]
    dash_quore = DASH.objects.all()[DASH.objects.count() - 7:]

    return bitcoin_quore, ether_quore, litecoin_quore, ripple_quore, zcash_quore, dash_quore