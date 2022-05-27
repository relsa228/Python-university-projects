from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    adress = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    is_moderator = models.BooleanField(default=False)
