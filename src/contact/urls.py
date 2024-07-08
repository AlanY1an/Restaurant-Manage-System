from django.urls import path, include
from . import views


app_name = 'contact'

urlpatterns = [
    path('',views.send_email, name='send_email'),
    path('success/',views.send_success,name='send_success'),
]
