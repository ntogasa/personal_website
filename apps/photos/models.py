from django.db import models

# Create your models here.
class Photo(models.Model):
    alt = models.CharField(max_length=500, null=True)
    image = models.ImageField(null=False, blank=False)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)