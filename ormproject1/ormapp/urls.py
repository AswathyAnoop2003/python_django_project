from django.conf.urls import url
from ormapp import views

urlpatterns = [
              url(r'^getdata/', views.getdatafrommodel, name="front"),

    # url(r'^',views.index,name="index"),
]