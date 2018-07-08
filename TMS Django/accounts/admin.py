from django.contrib import admin
from . import models
from .models import Project,Profile,TimeSheet
# Register your models here.
@admin.register(Profile)
class AdminEmp(admin.ModelAdmin):
    list_display = ('id', 'emp_name', 'gender', 'job_position', 'salary' )
    list_editable = ('gender', 'salary','job_position',)

@admin.register(Project)
class AdminEmp(admin.ModelAdmin):
    list_display = ('id', 'project_name', )

@admin.register(TimeSheet)
class AdminEmp(admin.ModelAdmin):
    list_display = ('id', 'emp_name','start_time','end_time' )
    list_editable = ('emp_name','start_time', 'end_time',)
#admin.site.register(models.Profile)
#admin.site.register(models.Project)
#admin.site.register(models.TimeSheet)
