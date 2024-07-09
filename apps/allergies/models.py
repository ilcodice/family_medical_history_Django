from django.db import models
from apps.family_members.models import FamilyMember

#Create your models here.
class Allergies(models.Model):
    patient_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    allergy_id = models.AutoField(primary_key=True)
    allergies = models.CharField(max_length=20)



    class Meta:
        db_table = 'allergy'


    def __str__(self):
        return f"Patient_id: {self.patient_id} - Patient_allergy: {self.allergies}"


