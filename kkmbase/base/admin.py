# coding= utf-8
from django.contrib import admin


from .models import Phonenumber
from .models import Serviced
from .models import Worker
from .models import Inspection
from .models import Brand
from .models import Device
from .models import DeviceModel
from .models import ControlCashMachine
from .models import RegistrationData
from .models import Version

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
    ordering = ['-registration_date']
    extra = 1
class ControlCashMachineAdmin(admin.ModelAdmin):
    exclude = ('registration_data',)
    inlines = [RegistrationDataServiced]     
    
       
class DeviceModelServiced(admin.TabularInline):
    model = DeviceModel
    extra = 1
class ControlCashMachineServiced(admin.TabularInline):
    model = ControlCashMachine
    extra = 1

    
class BrandAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'фирма изготовитель', {'fields': ['brand_name',]})
    ]

    inlines = [DeviceModelServiced, ]

admin.site.register(Phonenumber, PhonenumberAdmin)
admin.site.register(Serviced, ServicedAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Inspection, InspectionAdmin)

admin.site.register(Device)

admin.site.register(DeviceModel)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ControlCashMachine, ControlCashMachineAdmin)
admin.site.register(RegistrationData)
admin.site.register(Version)