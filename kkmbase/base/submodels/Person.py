# coding= utf-8
from django.db import models
from django.db.models import CharField

class Person(models.Model):
    name = CharField(u'Имя', max_length=255)    
    class Meta:
        abstract = True  
        

