from django.contrib import admin

from .models import Encounter, Disease, DiagnosisDiseaseGroupEntry

admin.site.register(Encounter)
admin.site.register(Disease)
admin.site.register(DiagnosisDiseaseGroupEntry)

# Register your models here.
