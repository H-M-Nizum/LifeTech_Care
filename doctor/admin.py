from django.contrib import admin
from . import models
# Register your models here.

# for slug fields. auto fillup slug fields in admin panale
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(models.DesignationModel, DesignationAdmin)
admin.site.register(models.SpecializationModel, SpecializationAdmin)
admin.site.register(models.AvailableTimeModel)
admin.site.register(models.DoctorModel)
admin.site.register(models.ReviewModel)