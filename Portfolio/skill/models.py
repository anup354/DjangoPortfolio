from django.db import models

# Create your models here.
class skill(models.Model):
    skill_name=models.CharField(max_length=50)
    skill_percentage=models.CharField(max_length=3)
    
