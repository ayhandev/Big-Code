from django.contrib import admin
from .models import infa
# Register your models here.

@admin.register(infa)
class InfaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date')
