# coding= utf-8
from django.contrib import admin

from .models import Phonenumber
from .models import Serviced
from .models import Worker
from .models import Inspection
from .models import Device
from .models import DeviceName
from .models import FactoryName


class WorkerServiced(admin.TabularInline):
    model = Worker
    extra = 1
class PhonenumberServiced(admin.TabularInline):
    model = Phonenumber
    extra = 1
class ServicedAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'организация: ', {'fields': ['name', 'inn', 'address', 'inspection']}),
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
    
class DeviceNameServiced(admin.TabularInline):
    model = DeviceName
    extra = 1
class FactoryNameServiced(admin.TabularInline):
    model = FactoryName
    extra = 1
    
class DeviceAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'устройство: ', {'fields': ['device_name', 'factory_name', 'factory_number', 'inventory_number']}),
    ]
    #inlines = [DeviceNameServiced, FactoryNameServiced]

admin.site.register(Phonenumber, PhonenumberAdmin)
admin.site.register(Serviced, ServicedAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Inspection)
admin.site.register(Device)
#admin.site.register(DeviceName)
#admin.site.register(FactoryName)