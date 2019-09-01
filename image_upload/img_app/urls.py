from django.conf.urls import url
from img_app import views

urlpatterns = [
    url(r'^form/', views.homePage, name="temp"),

    # url(r'^',views.index,name="index"),
]