# Generated by Django 3.2.13 on 2022-05-30 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_singup_page', '0005_alter_users_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]