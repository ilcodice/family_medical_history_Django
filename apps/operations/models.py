from django.db import models
from apps.family_members.models import FamilyMember
# Create your models here.
class Operation(models.Model):
    patient_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    operation_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=50)
    doctor = models.CharField(max_length=30)
    date = models.IntegerField(null=True, blank=True)  # You might want to use DateField instead
    place = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    costs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 

    class Meta():
        db_table = 'operations'

    
    def __str__(self):
        return f'Patient_Name: {self.patient_id}- operation: {self.operation}'