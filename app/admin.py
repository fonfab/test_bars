from django.contrib import admin
from app import models

# Register your models here.

admin.site.register(models.Recruit)
admin.site.register(models.Sith)
admin.site.register(models.Planet)

admin.site.register(models.TestTrials)
admin.site.register(models.Question)
admin.site.register(models.QuestionAsk)

