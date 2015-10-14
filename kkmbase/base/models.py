# coding= utf-8
from django.db import models
from django.db.models import CharField
from django.db.models import ForeignKey
#from submodels.RegistrationInformation import DeregistrationDate

class Organization(models.Model):
    name    = CharField(u'Название: ', blank=True, max_length=255, null=True)
    address = CharField(u'Адрес: ', blank=True, max_length=255, null=True)    
    class Meta:
        abstract = True
        
class Person(models.Model):
    name = CharField(u'Имя', max_length=255)    
    class Meta:
        abstract = True
        
class Phonenumber(models.Model):
    number = CharField(u'номер', max_length=255, unique=True)
    details = CharField(u'описание', max_length=255, blank=True, null=True)
    worker = models.ForeignKey('Worker', verbose_name=u'сотрудник', blank=True, null=True)
    organization = ForeignKey('Serviced', verbose_name=u'организация', blank=True, null=True)
    inspection = ForeignKey('Inspection', verbose_name=u'налоговая инспекция', blank=True, null=True)
    def __unicode__(self):    
        if not self.worker == None: abonent = self.worker
        if not self.organization == None: abonent = self.organization
        if not self.inspection == None: abonent = self.inspection        
        return u'%s/%s' % (abonent, self.number)
    class Meta:
        verbose_name = u'телефонный номер'
        verbose_name_plural = u'телефонные номера'

class Serviced(Organization):
    inn = CharField(u'ИНН', max_length=12, blank=True)
    inspection = ForeignKey('Inspection', verbose_name=u'налоговая инспекция', blank=True, null=True)
    def __unicode__(self):
        return u'%s, %s' % (self.name, self.address)
    class Meta:
        verbose_name = u'обслуживаемая организация'
        verbose_name_plural = u'обслуживаемые организации'
    
class Worker(Person):
    workplace = ForeignKey(Serviced, verbose_name = u'место работы', blank=True, null=True)    
    status = CharField(verbose_name=u'должность',max_length=255, blank=True, null=True)    
    def __unicode__(self):
        if unicode(self.workplace).split()[0] == u'None':
            return u'%s, %s'% (self.name, self.status)
        return u'%s, %s, %s' % (self.name, self.status, unicode(self.workplace).split()[0].replace(',', ''))        
    class Meta:
        ordering =('workplace',)
        verbose_name = u'сотрудник'
        verbose_name_plural = u'сотрудники'
        
class Inspection(Organization):
    number = CharField(u'номер налоговой инспекции', max_length=8, unique=True)    
    def __unicode__(self):
        return u'ИФНС № %s' % (self.number)
    class Meta:
        verbose_name = u'налоговая инспекция'
        verbose_name_plural = u'налоговые инспекции'
        
class DeviceModel(models.Model):
    model_name = CharField(u'название/модель', max_length=255, blank=True, null=True)
    factory = ForeignKey('Factory', verbose_name=u'производитель', blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.model_name)
    class Meta:
        verbose_name = u'вид техники'
        verbose_name_plural = u'виды техники'
        
class Factory(models.Model):
    factory_name = CharField(u'производитель: ', max_length=255)
    def __unicode__(self):
        return u'%s' % (self.factory_name)
    class Meta:
        verbose_name = u'производитель'
        verbose_name_plural = u'производители'
    
class AbstractDevice(models.Model):
    factory_number = CharField(u'заводской номер', blank=True, max_length=255, null=True)
    inventory_number = CharField(u'инвентарный номер', blank=True, max_length=255, null=True)
    class Meta:
        abstract = True
        
class Device(AbstractDevice):
    device_model = ForeignKey('DeviceModel', verbose_name=u'модель', blank=True, null=True)
    def __unicode__(self):
        return u'%s/%s/%s' % (self.device_model.factory, 
                              self.device_model.model_name, 
                              self.factory_number)
    class Meta:
        verbose_name = u'устройство'
        verbose_name_plural = u'другие устройства'

class ControlCashMachine(AbstractDevice):
    device_model = ForeignKey('DeviceModel', verbose_name=u'модель', blank=True, null=True)
    inspection = ForeignKey('Inspection', verbose_name=u'налоговая инспекция', blank=True, null=True)
    serviced = ForeignKey('Serviced', verbose_name=u'организация', blank=True, null=True)
    registration_data = ForeignKey('RegistrationData', verbose_name=u'сведения о регистрации', blank=True, null=True)
    
    def __unicode__(self):
        return u'%s/%s' % (self.device_model.model_name, self.factory_number)
    class Meta:
        verbose_name = u'ККМ'
        verbose_name_plural = u'ККМ'

class RegistrationData(models.Model):
    control_cash_machine = ForeignKey('ControlCashMachine', verbose_name=u'ККМ', blank=True, null=True)
    registration_date = models.ForeignKey('RegistrationDate', verbose_name=u'дата регистрации', blank=True, null=True)
    deregistration_date = models.ForeignKey('DeregistrationDate', verbose_name=u'дата снятия с регистрации', blank=True, null=True)
    def __unicode__(self):
        return u'%s' % (self.deregistration_date)
    class Meta:
        verbose_name = u'сведение о регистрации'
        verbose_name_plural = u'сведения о регистрациях'
 


















        
    

