from django.db import models
from apps.family_members.models import FamilyMember  # Importing FamilyMember model

class Appointment(models.Model):
    patient_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    appointment_id = models.AutoField(primary_key=True)
    doctor_speciality = models.CharField(max_length=50)
    doctor_name = models.CharField(max_length=50)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_address = models.CharField(max_length=50)
    accompany = models.CharField(max_length=30)

    class Meta:
        db_table = 'appointments'

    def __str__(self):
        return f"Patient_ID: {self.patient_id} - Doctor: {self.doctor_name} - Appointments: {self.appointment_address} - Date: {self.appointment_date} - Time: {self.appointment_time}"
