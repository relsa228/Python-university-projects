from django.contrib import admin
from .models import UserCryptoAcc, UserUsdAcc, UsersAvatars

admin.site.register(UserCryptoAcc)
admin.site.register(UserUsdAcc)
admin.site.register(UsersAvatars)
