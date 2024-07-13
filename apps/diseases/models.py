from django.db import models
from apps.medicaments.models import Medicine

class Disease(models.Model):
    #medicament_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    disease_id = models.AutoField(primary_key=True)
    disease = models.CharField(max_length=50)

    class Meta:
        db_table = 'diseases'

    def __str__(self):
        return f"Disease: {self.disease}" # so will se Disease name

class FamilyDisease(models.Model):
    patient_id = models.ForeignKey('family_members.FamilyMember', on_delete=models.CASCADE)
    disease_id = models.ForeignKey('diseases.Disease', on_delete=models.CASCADE)

    class Meta:
        db_table = 'family_diseases'

    def __str__(self):
        return f"FamilyMember: {self.patient_id} - Disease: {self.disease_id}"
