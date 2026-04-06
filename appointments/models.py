from django.db import models

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    appointment_status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled')

    
    def __str__(self):
        return f"{self.patient.name} with {self.doctor.name} at {self.appointment_time.strftime('%Y-%m-%d %H:%M')}"