from django.db import models

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

FEATURE = (
    (0, 'Do not feature'),
    (1, 'Feature')
)

# Create your models here.
class WritingPieces(models.Model):
    title = models.CharField(max_length=200)
    byline = models.CharField(max_length=500, default='Nikk Ogasa')
    publication = models.CharField(max_length=200, default='')
    syndication = models.CharField(max_length=200, blank=True, null=True)
    pub_link = models.URLField(null=True, blank=True)
    pdf_link = models.URLField(null=True, blank=True)
    date = models.DateField()
    image = models.ImageField(upload_to='featured_images/', null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    feature = models.IntegerField(choices=FEATURE, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
