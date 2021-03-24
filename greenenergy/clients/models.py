from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    image1 = models.ImageField(upload_to='clients/', null=True, blank=True)

    def __str__(self):
        return self.name
    