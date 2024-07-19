# Framework imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count

# Custom imports
from . import models
from apps.diseases.models import Disease
# Create your views here.

def home_page(request):
    
    # view can return valid formats like 
    # html, xml, json, etc
    # how to git distinct in ORM
    # Hint: use .distinct() and .count()
    engaged_fam_members_cnt = models.FamilyMember.objects.distinct('patient_id').count()
    total_disease_cnt = Disease.objects.count() # Disease is name of class
    response = f"""
        <html>
            <h1>Welcome to my MyApp App</h1>
            <p>{engaged_fam_members_cnt} fam_members!</p>
            <p>{total_disease_cnt} Total Diseases in Family
        </html>
    """
    
    # Return a response 
    return HttpResponse(response)

# templet View
# class way 
class HomePage(TemplateView):
    # specify the template to display
    template_name = 'home_page.html'