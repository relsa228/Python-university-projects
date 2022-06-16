import random
import smtplib

from user_page.models import UserCryptoAcc, UserUsdAcc, UsersAvatars
from .models import VerificateUser
from . import config as config


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
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(config.USER_EMAIL, config.USER_PASSWORD)

    code = random.randint(100000, 999999)
    message = f"{first_name} {last_name},\n\nСпасибо за регистрацию на нашей бирже! \n\nВаш код авторизации: " \
              f"{code} \n\nС уважением, администрация Borsa".encode("utf8")

    server.sendmail(config.USER_EMAIL, email, message)
    server.quit()

    new_user = VerificateUser(username=username, is_verificate=code)
    new_user.save()


def verificate_user(code) -> bool:
    if VerificateUser.objects.filter(is_verificate=code).exists():
        ver_user = VerificateUser.objects.get(is_verificate=code)
        ver_user.is_verificate = "true"
        ver_user.save()
        return True
    else:
        return False


def verifiction_check(username):
    check = VerificateUser.objects.get(username=username)
    if check.is_verificate == "true":
        return True
    else:
        return False
