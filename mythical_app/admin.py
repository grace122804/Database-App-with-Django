from django.contrib import admin
from .models import (
    Ability, Diagnosis, Employee, Invoice, LineItem, Observation,
    Owner, Patient, PatientAbility, Payment, ProcedureDefinition,
    Universe, Visit, VisitDiagnosis, VisitProcedure, CareNote
)


class CareNoteAdmin(admin.ModelAdmin):
    list_display = ('patient', 'created_at', 'follow_up_date', 'resolved')
    list_filter = ('resolved', 'created_at')
    search_fields = ('patient__name', 'note')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


# Register your models here.
admin.site.register(Ability)
admin.site.register(Diagnosis)
admin.site.register(Employee)
admin.site.register(Invoice)
admin.site.register(LineItem)
admin.site.register(Observation)
admin.site.register(Owner)
admin.site.register(Patient)
admin.site.register(PatientAbility)
admin.site.register(Payment)
admin.site.register(ProcedureDefinition)
admin.site.register(Universe)
admin.site.register(Visit)
admin.site.register(VisitDiagnosis)
admin.site.register(VisitProcedure)
admin.site.register(CareNote, CareNoteAdmin)
