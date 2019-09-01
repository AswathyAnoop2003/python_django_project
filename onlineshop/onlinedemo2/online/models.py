from django.db import models

# Create your models here.
from django.urls import reverse

class Product(models.Model):
    name=models.CharField(max_length=268)
    price=models.IntegerField()
    warrenty=models.IntegerField()
    waterRes=models.CharField(max_length=268)
    display=models.CharField(max_length=268)
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("online:detail",kwargs={'pk':self.pk})


class Customer(models.Model):
    name=models.CharField(max_length=268)
    home=models.CharField(max_length=268)
    area=models.CharField(max_length=268)
    town=models.CharField(max_length=268)
    state=models.CharField(max_length=268)
    pin=models.IntegerField()

    def __str__(self):
        return self.name