# coding= utf-8
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

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

class PhonenumberInline(GenericTabularInline):
    model = Phonenumber
    extra = 1    
class PhonenumberAdmin(admin.ModelAdmin):
    #fieldsets = [(u'Введите номер телефона.', {'fields': ['number', 'details', ]}),]
    pass
class ServicedAdmin(admin.ModelAdmin):
	inlines = [PhonenumberInline,]
class WorkerAdmin(admin.ModelAdmin):
	inlines = [PhonenumberInline,]
class InspectionAdmin(admin.ModelAdmin):
	inlines = [PhonenumberInline,]
    
admin.site.register(Phonenumber, PhonenumberAdmin)
admin.site.register(Serviced, ServicedAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Device)
admin.site.register(DeviceModel)
admin.site.register(Brand)
admin.site.register(ControlCashMachine)
admin.site.register(RegistrationData)
admin.site.register(Version)
