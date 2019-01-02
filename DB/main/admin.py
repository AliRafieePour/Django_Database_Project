from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.students)
class studentsAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'major', 'type_degree')

@admin.register(models.majors)
class majorsAdmin(admin.ModelAdmin):
    list_display = ('major_id', 'dept')

@admin.register(models.dept)
class deptAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenum')

@admin.register(models.workers)
class workersAdmin(admin.ModelAdmin):
    list_display = ('worker_id', 'worker_name', 'worker_duty')

@admin.register(models.rooms)
class roomsAdmin(admin.ModelAdmin):
    list_display = ('room_id', 'room_admin', 'room_statue')

@admin.register(models.dorms)
class dormsAdmin(admin.ModelAdmin):
    list_display = ('dorm_id', 'dorm_name', 'num_rooms', 'num_facil', 'dorm_admin', 'phonenum')