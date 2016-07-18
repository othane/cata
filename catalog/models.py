from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class CatalogItem(models.Model):
    """
    Represents a single item in the catalog, ie 12 pk coke only $8.99
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='catalog')
    desc = models.CharField('description', max_length=256)
    thumb = models.ImageField('thumbnail', upload_to=FileSystemStorage(''))
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateField()
    start = models.DateField()
    end = models.DateField()
