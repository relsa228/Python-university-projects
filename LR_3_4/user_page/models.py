from django.db import models


class UserCryptoAcc(models.Model):
    username = models.TextField("Имя пользователя")
    crypto_ticker = models.TextField("Тикер криптовалюты")
    token_count = models.TextField("Количество токенов")
    usd_count = models.TextField("Стоймость в долларах")
    usd_in = models.TextField("Вложения в долларах")

    def __str__(self):
        return self.username


class UserUsdAcc(models.Model):
    username = models.TextField("Имя пользователя")
    usd_count = models.TextField("Стоймость в долларах")

    def __str__(self):
        return self.username


class UsersAvatars(models.Model):
    username = models.TextField("Имя пользователя")
    imgur_link = models.TextField("Ссылка на аватарку")
    imgur_link_small = models.TextField("Ссылка на миниатюру")

    def __str__(self):
        return self.username
