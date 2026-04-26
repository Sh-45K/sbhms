from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from django.utils.decorators import method_decorator
from django.views import View 
from django.views.generic import ListView
from .forms import AppointmentForm

# Create your views here.
# @login_required
# def appointment_list(request):
#     appoinments = Appointment.objects.all()
#     return render(request, 'app_list.html', {'appointments': appoinments})

@method_decorator(login_required, name='dispatch')
class AppointmentListView(ListView):
    
    def get(self,request):
        appointment = Appointment.objects.all()
        return render(request, 'app_list.html', {'appointments': appointment})  
    
    def post(self,request):
        pass


# ✅ CREATE
@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/create.html', {'form': form})   

# ✅ EDIT
@login_required
def edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'appointments/edit.html', {'form': form})

# ✅ DELETE
@login_required
def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments')

    return render(request, 'appointments/delete.html', {'appointment': appointment})


