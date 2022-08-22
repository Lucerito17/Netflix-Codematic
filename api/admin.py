from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=['id', 'name','poster','gender']
    pass

@admin.register(models.Gender)
class GenderAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    pass