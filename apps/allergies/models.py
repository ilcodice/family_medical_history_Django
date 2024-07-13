from django.db import models

#Create your models here.
class Allergy(models.Model):
    #patient_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE) # patient
    allergy_id = models.AutoField(primary_key=True) # allergy
    allergies = models.CharField(max_length=20) # allergy

    # class Meta:
    #     db_table = 'allergies'


    # def __str__(self):
    #     return f"Allergy: {self.allergy_id}"


class FamilyAllergy(models.Model):
    allergy_id = models.ForeignKey('allergies.Allergy', on_delete=models.CASCADE) #on_delete for deleting if relation is deleted
    patient_id = models.ForeignKey('family_members.FamilyMember', on_delete=models.CASCADE)

    class Meta:
        db_table = 'family_allergies'

    def __str__(self):
        return f"{self.patient_id} - {self.allergy_id}"
