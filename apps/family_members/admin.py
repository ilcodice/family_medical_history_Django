from django.contrib import admin
from .models import FamilyMember
from apps.allergies.models import FamilyAllergy
from apps.diseases.models import FamilyDisease
from apps.appointments.models import Appointment
# Register your models here.

class FamilyAllergyInline(admin.StackedInline):
    model = FamilyAllergy
    extra = 1

class FamilyDiseaseInLine(admin.StackedInline):
    model = FamilyDisease
    extra = 1

class FamilyAppointmentsInLine(admin.StackedInline):
    model = Appointment
    extra = 1


# this class is for print the fname, lname, pid,place in nice shape
class FamilyMemberAdmin(admin.ModelAdmin):
    
    inlines = (FamilyAllergyInline, FamilyDiseaseInLine,FamilyAppointmentsInLine)
    search_fields = ('first_name', 'last_name','allergies')
    list_display = ('first_name', 'last_name', 'patient_id', 'place')
    list_filter = ('allergies','diseases') # filter for each column 




admin.site.register(FamilyMember,FamilyMemberAdmin)
#admin.site.register(FamilyAppointmentsInLine)