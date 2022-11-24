from django.db import models

# Create your models here.
class study_detail(models.Model):
    institution=models.CharField(max_length=50)
    study_program=models.CharField(max_length=50)
    start_date=models.CharField(max_length=50)
    end_date=models.CharField(max_length=50)
    
