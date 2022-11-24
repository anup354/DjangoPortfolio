from django.db import models

# Create your models here.
class desc(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    ak_img=models.FileField(upload_to="profile_img/",null=True,default=None)
