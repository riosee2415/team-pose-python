from django.contrib import admin
from . import models


@admin.register(models.ContactModel)
class ContactModelAdmin(admin.ModelAdmin):

    pass
