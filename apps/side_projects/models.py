from django.db import models

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

# Create your models here.
class SideProject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    link = models.URLField()
    status = models.IntegerField(choices=STATUS, default=0)