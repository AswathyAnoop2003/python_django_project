from django.urls import path

from online import views
app_name="online"

urlpatterns = [
    path('',views.productlistview.as_view(),name='list'),
    path('<int:pk>/',views.productdetailsview.as_view(),name='detail'),

]