from django.db import models

# Create your models here.
class Testmony(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image1 = models.ImageField(upload_to='testmonies/', null=True, blank=True)    
    product = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self):
        return self.first_name