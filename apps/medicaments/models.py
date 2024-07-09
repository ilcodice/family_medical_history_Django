from django.db import models
from apps.family_members.models import FamilyMember
# Create your models here.

class Medicaments(models.Model):
    patient_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE) # FOREIGN KEY
    Medicament_id = models.AutoField(primary_key=True) # SERIAL PRIMARY KEY
    medicament = models.CharField(max_length=50)
    for_what = models.TextField()
    type = models.CharField(max_length=50)
    costs = models.DecimalField(max_digits=10, decimal_places=2) 
    dose = models.IntegerField()
    when_to_use = models.CharField(max_length=30)

    class Meta():
        db_table = 'medicaments'


    def __str__(self):
        return f"Patient Name: {self.patient_id} - Medicament: {self.medicament}"