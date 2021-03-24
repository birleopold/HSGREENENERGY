from django.db import models

# Create your models here.


    
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    product = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.first_name
        
    



