from django.db import models

# Create your models here.


class Cine(models.Model):   #Table definition
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=20)
    year=models.IntegerField()
    img= models.FileField(upload_to="cine/img",null=True,blank=True)

    def __str__(self):
        return self.name



