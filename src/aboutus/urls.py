from django.urls import path, include
from . import views


app_name = 'aboutus'

urlpatterns = [
    path('',views.aboutus_list, name='aboutus_list'),


]
