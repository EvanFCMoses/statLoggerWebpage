from django.contrib import admin

from .models import Encounter, Disease, DiagnosisDiseaseGroupEntry

class DiseaseInline(admin.TabularInline):
	model = DiagnosisDiseaseGroupEntry
	extra=0

class EncounterAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)

	inlines = [DiseaseInline]


admin.site.register(Encounter, EncounterAdmin)
# Register your models here.
