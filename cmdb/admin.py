from django.contrib import admin
from cmdb import models

# Register your models here.

admin.site.site_header = "Foxconn PDSS"

admin.site.register(models.Colors)
admin.site.register(models.Clothes)
admin.site.register(models.Child)
admin.site.register(models.Ball)
