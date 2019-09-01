from django.urls import path

from adminView import views
app_name="adminView"

urlpatterns = [
    path('',views.productlist.as_view(),name='list'),
    path('<int:pk>/',views.productdetailsview.as_view(),name='detail'),
    path('delete/<int:pk>', views.productDeleteView.as_view(), name='delete'),
    path('create/', views.productCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.productUpdateView.as_view(), name='update')

]