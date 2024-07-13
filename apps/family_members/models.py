from django.contrib.auth.models import AbstractUser
from django.db import models

# because it is user model so i add AbstractUser to the class 
# because Abstract class have first_name and last_name so i dont have to add them 
class FamilyMember(AbstractUser):
    patient_id = models.AutoField(primary_key=True) # SERIAL PRIMARY KEY
    place = models.CharField(max_length=20) # VARCHAR
    # here we connect allergies to allergy.Allergy throught FamAllerg , null, blank = True so myabe one member do not have allergy 
    allergies = models.ManyToManyField("allergies.Allergy",related_name="family_members",through="allergies.FamilyAllergy",blank=True)
    diseases = models.ManyToManyField("diseases.Disease",related_name="family_members",through="diseases.FamilyDisease",blank=True)
    medicaments = models.ManyToManyField("medicaments.Medicine",related_name="family_members",through="medicaments.FamilyMedicine",blank=True)


    class Meta:
        db_table = 'family_members'
        verbose_name = 'Family Member'
        verbose_name_plural = 'Family Members'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
