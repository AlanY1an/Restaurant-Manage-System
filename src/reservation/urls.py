from django.urls import path, include
from . import views


app_name = 'reservation'

urlpatterns = [
    path('',views.reserve_table, name='reserve_table'),

]
