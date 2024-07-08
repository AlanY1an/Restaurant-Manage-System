from django.shortcuts import render
from django.contrib import messages


# Create your views here.
from .models import Reservation
from reservation.models import Reservation
from .forms import ReserveTableForm

def reserve_table(request):
    reserve_form = ReserveTableForm()
    
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
            messages.success(request, 'Your reservation has been successfully submitted!')


    context = {'form':reserve_form}

    return render(request, 'Reservation/reservation.html', context)

