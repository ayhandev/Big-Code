from django.contrib import admin
from .models import infa, PublishedCode, Messenger
# Register your models here.

@admin.register(infa)
class InfaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date')

@admin.register(PublishedCode)
class PublishedCodeAdmin(admin.ModelAdmin):
    ...


@admin.register(Messenger)
class MessengerAdmin(admin.ModelAdmin):
    ...