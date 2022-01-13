from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Car(models.Model):
    modl = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    rentrate = models.IntegerField()
    buyrate = models.IntegerField()
    odometer = models.IntegerField()
    IsAvailable = models.BooleanField()
    Customer = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='RentedCab')

    def __str__(self):
        return self.modl


