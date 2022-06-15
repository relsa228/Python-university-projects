from user_page.models import UserCryptoAcc, UserUsdAcc, UsersAvatars
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random


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


def create_avatar_link(username):
    new_avatar = UsersAvatars(username=username, imgur_link="https://i.imgur.com/VlNyyn3.png")
    new_avatar.save()


def send_aprove_mail(email, username, first_name, last_name):
    code = random.randint(100000, 999999)
    message = f"{first_name} {last_name},\n\nблагодарим вас за регистрацию на нашей бирже!\n\nВаш код подтверждения: {code}" \
              f"\n\nС уважением, администрация Borsa"
    send_mail(subject='Регистрация на бирже Borsa', message=message, from_email='borsanonreply@gmail.com', recipient_list=
              [email], fail_silently=True)


