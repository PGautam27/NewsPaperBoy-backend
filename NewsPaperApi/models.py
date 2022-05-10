from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=122)
    user_phone = models.IntegerField()
    user_email = models.EmailField()
    user_password = models.CharField(max_length=122)
    user_address = models.TextField()