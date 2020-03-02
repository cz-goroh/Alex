import datetime
import hashlib
from django.contrib import admin
from django import forms
from .models import (Teachers, Places, Appointments)
from .fields import ColorField

# Register your models here.


class AppointmentsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        ColorField: {'widget': forms.TextInput(attrs={'type': 'color', \
            'style': 'height: 20px; width: 100px;'})}
    }

    def save_model(self, request, obj, form, change):
        # if not change:
        # print(hashlib.sha1(str(datetime.datetime.now().timestamp()).encode('utf-8')))
        obj.appointment_id = str(hashlib.sha1(str( datetime.datetime.now().timestamp()).encode('utf-8')).hexdigest())
        obj.save()


admin.site.register(Teachers)
admin.site.register(Places)
admin.site.register(Appointments, AppointmentsAdmin)
