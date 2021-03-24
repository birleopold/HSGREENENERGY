from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telephone = models.CharField(max_length=200)
    staff_role = models.CharField(max_length=200)    
    image1 = models.ImageField(upload_to='products/', null=True, blank=True)
   

    def __str__(self):
        return self.first_name
