# coding= utf-8
from django.db import models
from django.db.models import CharField

class Organization(models.Model):
    name = CharField(u'Название: ', blank=True, max_length=255, null=True)
    address = CharField(u'Адрес: ', blank=True, max_length=255, null=True)
    description = CharField(u'описание: ', blank=True, max_length=255, null=True)
    work_hours = CharField(u'часы работы: ', blank=True, max_length=255, null=True)
    class Meta:
        abstract = True
        

