# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    return render(request,'Form2.html')

# Create your views here.
