from django.urls import path
from . import views

app_name = 'african_cities'

urlpatterns = [
    path('', views.city_list, name='city_list'),
] 