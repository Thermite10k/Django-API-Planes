from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Parts)
admin.site.register(models.Planes)
admin.site.register(models.Operators)
admin.site.register(models.faultyPart)
