from django.contrib import admin
from .models import  *

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskProgress)
class TaskProgressAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskStatus)
class TasksStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskType)
class TasksTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(PhoneCall)
class PhoneCall(admin.ModelAdmin):
    pass