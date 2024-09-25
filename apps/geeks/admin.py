from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id']