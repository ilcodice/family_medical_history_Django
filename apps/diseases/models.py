from django.db import models #importing models to set types for columns
from apps.family_members.models import FamilyMember
from apps.medicaments.models import Medicaments
# Create your models here.

class Diseases(models.Model):
    patient_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    medicament_id = models.ForeignKey(Medicaments, on_delete=models.CASCADE)
    disease = models.CharField(max_length= 50)

    class Meta:
        db_table = 'diseases'

    def __str__(self):
        return f"Patient Name: {self.patient_id} - Disease: {self.disease}"