from django.contrib import admin
from .models import Task


class TaskModel(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'due_date', 'status')
    search_fields =('title', 'description')
# Register your models here.
admin.site.register(Task, TaskModel)