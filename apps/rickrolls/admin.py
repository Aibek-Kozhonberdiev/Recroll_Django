from django.contrib import admin

from . import models


@admin.register(models.RickrollUrl)
class AdminRickrollUrl(admin.ModelAdmin):
    pass
