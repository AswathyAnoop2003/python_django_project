# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ormapp.models import Employee

from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.


def  getdatafrommodel(request):
    name_list=Employee.objects.order_by('id')
    email_dict={"Employee":name_list}
    return  render(request,'front1.html',email_dict)
