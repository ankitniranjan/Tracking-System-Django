from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.BigIntegerField()
    reg_no = models.CharField(max_length=60)

class ActiveUser(models.Model):
    registered_id = models.IntegerField(default=None)
    fullname = models.CharField(max_length=60)
    reg_no = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    speed = models.CharField(max_length=60)
    time = models.TimeField()