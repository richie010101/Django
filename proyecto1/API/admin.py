from django.contrib import admin
from API.models import Ejemplo

@admin.register(Ejemplo)
class PodtAdmin(admin.ModelAdmin):
    list_display=['id','nombre'] 

# Register your models here.
