from django.shortcuts import render

# Create your views here.
from online.models import Product
from django.urls import reverse_lazy

from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

# Create your views here.
class productlist(ListView):
    model=Product

class productdetailsview(DetailView):
    context_object_name = 'product_details'
    model = Product
    template_name = 'adminView/product_detail.html'
    # template_name='online/product_list.html'

class productDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("adminView:list")


class productCreateView(CreateView):
    fields = ("name","price","warrenty","waterRes","display","image")
    model = Product


class productUpdateView(UpdateView):
    fields = ("name","price")
    model = Product