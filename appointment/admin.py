from django.contrib import admin
from .models import AppiontmentModel
# Register your models here.

class AppiontmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name', 'appointment_status', 'appointment_type', 'symptop', 'time', 'cancel']

    def patient_name(self, obj):
        return obj.patient.user.first_name
    def doctor_name(self, obj):
        return obj.doctor.user.first_name

admin.site.register(AppiontmentModel, AppiontmentAdmin)