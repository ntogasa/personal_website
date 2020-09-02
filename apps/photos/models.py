from django.db import models

STATUS = (
    (0, 'Hold'),
    (1, 'Publish')
)

# Create your models here.
class Photo(models.Model):
    alt = models.CharField(max_length=500, null=True)
    image = models.ImageField(null=False, blank=False, upload_to='photos')
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

