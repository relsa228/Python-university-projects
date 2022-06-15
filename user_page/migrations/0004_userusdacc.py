# Generated by Django 3.2.13 on 2022-06-06 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0003_auto_20220606_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUsdAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(verbose_name='Имя пользователя')),
                ('usd_count', models.TextField(verbose_name='Стоймость в долларах')),
            ],
        ),
    ]
