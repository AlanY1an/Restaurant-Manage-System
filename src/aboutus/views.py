from django.shortcuts import render

# Create your views here.
from .models import AboutUS, Why_Choose_Us, Chef

def aboutus_list(request):
    about = AboutUS.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()
    chef = Chef.objects.all()

    context = {
        'about': about,
        'why_choose_us': why_choose_us,
        'chef': chef,
    }
    return render(request, 'aboutus/about.html', context)

