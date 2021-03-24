from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='products/', null=True, blank=True)
    image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title