from django.contrib import admin
from .models import Appointment
# Register your models here.
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('patient_id','appointment_date','appointment_time', 'appointment_address','accompany')

    

admin.site.register(Appointment,AppointmentsAdmin)
