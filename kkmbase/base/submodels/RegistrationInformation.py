# coding= utf-8
from django.db import models
from django.db.models import CharField
#from ...base.models import ControlCashMachine


class RegistrationDate(models.Model):
    registration_date = models.DateField(verbose_name=u'дата регистрации', blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.registration_date)
    class Meta:
        verbose_name = u'дата регистрации'
        verbose_name_plural = u'даты регистраций'
        
class DeregistrationDate(models.Model):
    deregistration_date = models.DateField(verbose_name=u'дата снятия с регистрации', blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.deregistration_date)
    class Meta:
        verbose_name = u'дата снятия с регистрации'
        verbose_name_plural = u'даты снятий с регистраций'    
        
