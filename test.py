# allergies/models

# from django.db import models

# #Create your models here.
# class Allergy(models.Model):
#     #patient_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE) # patient
#     allergy_id = models.AutoField(primary_key=True) # allergy
#     allergies = models.CharField(max_length=20) # allergy



#     class Meta:
#         db_table = 'allergy'



#     def __str__(str):
#         return f"{self.allergies}"


# class FamilyAllergy(models.Model):
#     allergy_id = models.ForeignKey('allergies.Allergy', on_delete=models.CASCADE) #on_delete for deleting if relation is deleted
#     patient_id = models.ForeignKey('family_members.FamilyMember', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'family_allergies'

#     def __str__(self):
#         return f"{self.patient_id} - {self.allergy_id}"

# disease

# from django.db import models #importing models to set types for columns
# from apps.family_members.models import FamilyMember
# from apps.medicaments.models import Medicine
# # Create your models here.

# class Disease(models.Model):
#     #patient_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
#     medicament_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
#     disease_id = models.AutoField(primary_key=True)
#     disease = models.CharField(max_length= 50)



    
#     class Meta:
#         db_table = 'diseases'

#     def __str__(self):
#         return f"Disease: {self.disease}"
    
# #class FamilyDisease(models.Model):
#    # patient_id = models.ForeignKey('family_members.FamilyMember', on_delete=models.CASCADE)
#    # disease = models.ForeignKey('diseases.Disease', on_delete=models.CASCADE)

# this model is user model 






# from django.contrib.auth.models import AbstractUser
# from django.db import models


# # because it is user model so i add AbstractUser to the class 
# # because Abstract class have first_name and last_name so i dont have to add them 
# class FamilyMember(AbstractUser):
#     patient_id = models.AutoField(primary_key=True) # SERIAL PRIMARY KEY
#     place = models.CharField(max_length=20) # VARCHAR
#     # here we connect allergies to allergy.Allergy throught FamAllerg , null, blank = True so myabe one member do not have allergy 
#     allergies = models.ManyToManyField("allergies.Allergy",related_name= "Allergy",through="allergies.FamilyAllergy", blank=True)
#     #diseases = models.ManyToManyField("disease.Dieases",related_name= "Disease", through="diseases.FamilyDisease", null=True, blank= True)


#     class Meta:
#         db_table = 'family_members'
#         verbose_name = 'Family Member'
#         verbose_name_plural = 'Family Members'

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"





