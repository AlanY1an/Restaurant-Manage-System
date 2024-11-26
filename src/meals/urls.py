from django.urls import path, include
from . import views


app_name = 'meals'

urlpatterns = [
    path('',views.meal_list, name='meal_list'),
    path('<slug:slug>', views.meal_detail, name = 'meal_detail'),
]
