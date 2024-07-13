from django.contrib import admin
from .models import Allergy, FamilyAllergy
# Register your models here.

class AllergyAdmin(admin.ModelAdmin):
    list_display = ('allergy_id','allergies')

admin.site.register(Allergy,AllergyAdmin)
admin.site.register(FamilyAllergy)