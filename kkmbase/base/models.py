# coding= utf-8
from django.db import models


class Organization(models.Model):
    name    = models.CharField(u'Название: ', max_length=255)
    address = models.CharField(u'Адрес: ', blank=True, max_length=255, null=True)    
    class Meta:
        abstract = True
        
class Person(models.Model):
    name = models.CharField(u'Имя', max_length=255)
    
    class Meta:
        abstract = True
        
class Phonenumber(models.Model):
    number = models.CharField(u'номер', max_length=255, unique=True)
    details = models.CharField(u'описание', max_length=255, blank=True, null=True)
    worker = models.ForeignKey('Worker', verbose_name=u'сотрудник', blank=True, null=True)
    organization = models.ForeignKey('Serviced', verbose_name=u'организация', blank=True, null=True)
    inspection = models.ForeignKey('Inspection', verbose_name=u'налоговая инспекция', blank=True, null=True)
    def __unicode__(self):
        return u'Номер: %s ' % (self.number)
    class Meta:
        verbose_name = u'телефонный номер'
        verbose_name_plural = u'телефонные номера'

class Serviced(Organization):
    inn = models.CharField(u'ИНН', max_length=12, blank=True)
    inspection = models.ForeignKey('Inspection', verbose_name=u'налоговая инспекция', blank=True, null=True)
    def __unicode__(self):
        return u'%s, %s' % (self.name, self.address)
    class Meta:
        verbose_name = u'обслуживаемая организация'
        verbose_name_plural = u'обслуживаемые организации'
    
class Worker(Person):
    workplace = models.ForeignKey(Serviced, verbose_name = u'место работы', blank=True, null=True)    
    status = models.CharField(verbose_name=u'должность',max_length=255, blank=True, null=True)    
    def __unicode__(self):
        if unicode(self.workplace).split()[0] == u'None':
            return u'%s, %s'% (self.name, self.status)
        return u'%s, %s, %s' % (self.name, self.status, unicode(self.workplace).split()[0].replace(',', ''))        
    class Meta:
        ordering =('workplace',)
        verbose_name = u'сотрудник'
        verbose_name_plural = u'сотрудники'
        
class Inspection(Organization):
    number = models.CharField(u'номер налоговой инспекции', max_length=8, unique=True)    
    def __unicode__(self):
        return u'ИФНС № %s' % (self.number)
    class Meta:
        verbose_name = u'налоговая инспекция'
        verbose_name_plural = u'налоговые инспекции'
        
class DeviceModel(models.Model):
    model_name = models.CharField(u'название/модель', max_length=255, blank=True, null=True)
    factory = models.ForeignKey('Factory', verbose_name=u'производитель', blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.model_name)
    class Meta:
        verbose_name = u'вид техники'
        verbose_name_plural = u'виды техники'
        
class Factory(models.Model):
    factory_name = models.CharField(u'производитель: ', max_length=255)
    def __unicode__(self):
        return u'%s' % (self.factory_name)
    class Meta:
        verbose_name = u'производитель'
        verbose_name_plural = u'производители'
    
class AbstractDevice(models.Model):
    factory_number = models.CharField(u'заводской номер', blank=True, max_length=255, null=True)
    inventory_number = models.CharField(u'инвентарный номер', blank=True, max_length=255, null=True)
    class Meta:
        abstract = True
        
class Device(AbstractDevice):
    device_model = models.ForeignKey('DeviceModel', verbose_name=u'модель', blank=True, null=True)
    def __unicode__(self):
        for c in dir(self.device_model.factory):
            print c
        return u'%s/%s' % (self.device_model.factory, self.device_model.model_name)
    class Meta:
        verbose_name = u'устройства'
        verbose_name_plural = u'другие устройства'
    
    

