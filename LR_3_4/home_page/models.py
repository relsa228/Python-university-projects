from django.db import models


class BTC(models.Model):
    ticket = models.TextField("Тикет")
    current_buy_price = models.TextField("Цена покупки")
    current_sell_price = models.TextField("Цена продажи")
    avg_price = models.TextField("Средняя цена")
    date = models.DateTimeField("Дата")

    def __str__(self):
        return self.ticket

class ETH(models.Model):
    ticket = models.TextField("Тикет")
    current_buy_price = models.TextField("Цена покупки")
    current_sell_price = models.TextField("Цена продажи")
    avg_price = models.TextField("Средняя цена")
    date = models.DateTimeField("Дата")

    def __str__(self):
        return self.ticket


class XRP(models.Model):
    ticket = models.TextField("Тикет")
    current_buy_price = models.TextField("Цена покупки")
    current_sell_price = models.TextField("Цена продажи")
    avg_price = models.TextField("Средняя цена")
    date = models.DateTimeField("Дата")

    def __str__(self):
        return self.ticket


class LTC(models.Model):
    ticket = models.TextField("Тикет")
    current_buy_price = models.TextField("Цена покупки")
    current_sell_price = models.TextField("Цена продажи")
    avg_price = models.TextField("Средняя цена")
    date = models.DateTimeField("Дата")

    def __str__(self):
        return self.ticket


class ZEC(models.Model):
    ticket = models.TextField("Тикет")
    current_buy_price = models.TextField("Цена покупки")
    current_sell_price = models.TextField("Цена продажи")
    avg_price = models.TextField("Средняя цена")
    date = models.DateTimeField("Дата")

    def __str__(self):
        return self.ticket


class DASH(models.Model):
    ticket = models.TextField("Тикет")
    current_buy_price = models.TextField("Цена покупки")
    current_sell_price = models.TextField("Цена продажи")
    avg_price = models.TextField("Средняя цена")
    date = models.DateTimeField("Дата")

    def __str__(self):
        return self.ticket
