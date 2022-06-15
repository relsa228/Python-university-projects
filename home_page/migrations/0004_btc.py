# Generated by Django 3.2.13 on 2022-05-31 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_delete_btc'),
    ]

    operations = [
        migrations.CreateModel(
            name='BTC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.TextField(verbose_name='Тикет')),
                ('current_buy_price', models.TextField(verbose_name='Цена покупки')),
                ('current_sell_price', models.TextField(verbose_name='Цена продажи')),
                ('avg_price', models.TextField(verbose_name='Средняя цена')),
                ('date', models.DateTimeField(verbose_name='Дата')),
            ],
        ),
    ]