from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.

admin.site.register(models.Person)
admin.site.register(models.Book)
admin.site.register(models.Barrowed_book)
admin.site.register(models.Category)
