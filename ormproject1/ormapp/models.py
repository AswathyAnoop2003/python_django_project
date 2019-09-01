# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=264,unique=True)
    Email=models.CharField(max_length=264,unique=True)
    salary=models.CharField(max_length=264)


    def __str__(self):
        return(self.Email)