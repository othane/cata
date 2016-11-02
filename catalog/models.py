from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class Store(models.Model):
    """
    Represents a store where items can be bought, ie Count Down Onehunga
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='store')
    desc = models.CharField('description', max_length=256)
    website = models.CharField('website', max_length=256)
    address = models.CharField('address', max_length=256)
    created = models.DateField()

    def __str__(self):
        return "Store[{}]:{}".format(self.id, self.desc)


class CatalogItem(models.Model):
    """
    Represents a single item in the catalog, ie 12 pk coke only $8.99
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='catalog')
    store = models.ManyToManyField(Store)
    desc = models.CharField('description', max_length=256)
    thumb = models.ImageField('thumbnail')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateField()
    start = models.DateField()
    end = models.DateField()


