from django.contrib import admin
from .models import Medicine, FamilyMedicine
# Register your models here.

admin.site.register(Medicine)
admin.site.register(FamilyMedicine)