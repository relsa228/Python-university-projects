from user_page.models import UserCryptoAcc, UserUsdAcc


def create_user_crypto_bills(username):
    new_btc_bill = UserCryptoAcc(username=username, crypto_ticker="BTC", token_count="0", usd_count="0", usd_in="0")
    new_btc_bill.save()

    new_btc_bill = UserCryptoAcc(username=username, crypto_ticker="ETH", token_count="0", usd_count="0", usd_in="0")
    new_btc_bill.save()

    new_btc_bill = UserCryptoAcc(username=username, crypto_ticker="ZEC", token_count="0", usd_count="0", usd_in="0")
    new_btc_bill.save()

    new_btc_bill = UserCryptoAcc(username=username, crypto_ticker="DASH", token_count="0", usd_count="0", usd_in="0")
    new_btc_bill.save()

    new_btc_bill = UserCryptoAcc(username=username, crypto_ticker="LTC", token_count="0", usd_count="0", usd_in="0")
    new_btc_bill.save()

    new_btc_bill = UserCryptoAcc(username=username, crypto_ticker="XRP", token_count="0", usd_count="0", usd_in="0")
    new_btc_bill.save()


def create_user_usd_bill(username):
    new_usd_bill = UserUsdAcc(username=username, usd_count="0")
    new_usd_bill.save()
