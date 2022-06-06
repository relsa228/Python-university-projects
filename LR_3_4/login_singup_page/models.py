from django.db import models


class VerificateUser(models.Model):
    username = models.TextField("username")
    is_verificate = models.BooleanField("is_verificate")

    def __str__(self):
        return self.username
