from django.contrib import admin
from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'email')