# coding= utf-8
from django.db import models
from django.db.models import CharField

class Brand(models.Model):
    brand_name = CharField(u'производитель: ', max_length=255)
    def __unicode__(self):
        return u'%s' % (self.brand_name)
    class Meta:
        verbose_name = u'производитель'
        verbose_name_plural = u'производители'    
        

