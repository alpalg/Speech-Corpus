from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Audio)
# admin.site.register(models.RussianText)
# admin.site.register(models.EnglishText)


admin.site.register(models.Participant)
admin.site.register(models.Phrase)
admin.site.register(models.Audio)
