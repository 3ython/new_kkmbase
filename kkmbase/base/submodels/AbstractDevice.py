# coding= utf-8
from django.db import models
from django.db.models import CharField

class AbstractDevice(models.Model):
    factory_number = CharField(u'заводской номер', blank=True, max_length=255, null=True)
    inventory_number = CharField(u'инвентарный номер', blank=True, max_length=255, null=True)
    class Meta:
        abstract = True  
        

