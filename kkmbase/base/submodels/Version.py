# coding= utf-8
from django.db import models
from django.db.models import CharField

class Version(models.Model):
    version = CharField(u'версия: ', max_length=255)
    description = CharField(u'описание: ', blank=True, max_length=255, null=True)
    def __unicode__(self):
        return u'%s' % (self.version)
    class Meta:
        verbose_name = u'версия'
        verbose_name_plural = u'версии'    
        

