from django.contrib import admin
from .models import Disease, FamilyDisease
# Register your models here.

class FamilyDiseaseInLine(admin.StackedInline):
    model = FamilyDisease
    extra = 1

admin.site.register(Disease)
admin.site.register(FamilyDisease)