from django.db import models
from accounts.models import *

# Create your models here.

class JobAdd(models.Model):
    JOBTYPE=(
        ('Full_Time','Full_time'),
        ('Part_time','Part_time'),
        ('Contract','Contract'),
        ('Internship','Internship'),
    )
    fk_company_pro=models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    job_type = models.CharField(max_length=100,choices=JOBTYPE)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_fields=models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    education_requirements = models.CharField(max_length=100)
    experience_requirements = models.CharField(max_length=100)
    skills_and_qualifications = models.TextField()
    application_deadline = models.DateTimeField()
    filled=models.BooleanField(default=False)
    vacancy=models.IntegerField(default=1)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)