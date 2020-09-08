from django.db import models


STATUS = (
    (0, 'Hold'),
    (1, 'Publish')
)


class Category(models.Model):
    """A single CharField which represents the category(s) a photo can fall into"""
    name = models.CharField(max_length=50)


class Photo(models.Model):
    """The model for photos which are to be displayed in the photo gallery"""
    alt = models.CharField(max_length=500, null=True)
    picture = models.ImageField(null=False, blank=False, upload_to='photos')
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ManyToManyField('Category', related_name='photos')

