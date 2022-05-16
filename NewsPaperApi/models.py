from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=122)
    user_phone = models.IntegerField()
    user_email = models.EmailField()
    user_password = models.CharField(max_length=122)
    user_address = models.TextField()


class Distributor(models.Model):
    distributor_name = models.CharField(max_length=122)
    distributor_phone = models.IntegerField(max_length=10)
    distributor_email = models.EmailField()
    distributor_password = models.CharField(max_length=122)
    distributor_address = models.TextField()
