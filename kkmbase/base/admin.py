# coding= utf-8
from django.contrib import admin

from .models import Phonenumber
from .models import Serviced
from .models import Worker
from .models import Inspection
from .submodels import Brand
from .models import Device
from .models import DeviceModel
from .models import ControlCashMachine
from .models import RegistrationData
#from .submodels import RegistrationDate
#from .submodels import DeregistrationDate
from .submodels import Version

class WorkerServiced(admin.TabularInline):
    model = Worker
    extra = 1
class PhonenumberServiced(admin.TabularInline):
    model = Phonenumber
    extra = 1
class ServicedAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'организация: ', {'fields': ['name', 'inn', 'address', 'inspection', 'work_hours']}),
    ]
    inlines = [WorkerServiced, PhonenumberServiced]   
    
class PhonenumberWorker(admin.TabularInline):
    model = Phonenumber
    extra = 1
class WorkerAdmin(admin.ModelAdmin):
    inlines = [PhonenumberWorker]

    
class PhonenumberAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Выберите абонента.', {'fields': ['worker', 'organization', 'inspection']}),
        (u'Введите номер телефона.', {'fields': ['number', 'details']}),
    ]
class InspectionAdmin(admin.ModelAdmin):
    exclude = ('name',)

    
class RegistrationDataServiced(admin.TabularInline):
    model = RegistrationData
    extra = 1
class ControlCashMachineAdmin(admin.ModelAdmin):
    inlines = [RegistrationDataServiced]     
    
       
class DeviceServiced(admin.TabularInline):
    model = Device
    extra = 1
class FactoryServiced(admin.TabularInline):
    model = Brand
    extra = 1
    
class DeviceAdmin(admin.ModelAdmin):    
    fieldsetsm = [
        (u'устройство: ', {'fields': ['device_model' ]})# 'factory_name']}),
    ]
    def model_name(self, instance):
        return instance.model_name
    #nlines = [FactoryServiced]# Serviced, FactoryServiced]

admin.site.register(Phonenumber, PhonenumberAdmin)
admin.site.register(Serviced, ServicedAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceModel)
admin.site.register(Brand)
admin.site.register(ControlCashMachine, ControlCashMachineAdmin)
#admin.site.register(RegistrationDate)
#admin.site.register(DeregistrationDate)
admin.site.register(RegistrationData)
admin.site.register(Version)