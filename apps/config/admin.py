from django.contrib import admin

from config import models

admin.site.register(models.Logo)
admin.site.register(models.SEOHome)
admin.site.register(models.GoogleAnalytics)
admin.site.register(models.Scripts)
