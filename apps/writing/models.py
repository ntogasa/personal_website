from django.db import models

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

# Create your models here.
class WritingPieces(models.Model):
    title = models.CharField(max_length=200)
    byline = models.CharField(max_length=5000, default='Nikk Ogasa')
    content = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    date = models.DateField()
    status = models.IntegerField(choices=STATUS, default=0)