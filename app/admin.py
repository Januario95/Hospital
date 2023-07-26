from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Patient, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'phone_number')
    list_display_links = ('id', 'first_name')
    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_to_patient', 'phone_number', 'disease',
                    'priority', 'completed', 'date', 'entry_date')
    list_editable = ('priority', 'completed',)
    save_on_top = True
    
    def link_to_patient(self, obj):
        link = obj.patient.pk
        return mark_safe(f'''
            <a href="/admin/app/patient/{link}/change/">
                {obj.patient}
            </a>
        ''')
    link_to_patient.short_description = 'Patient'

    def phone_number(self, obj):
        cell_number = obj.patient.phone_number
        return mark_safe(f'''
            <a href="tel:{cell_number}">{cell_number}</a>
        ''')
    phone_number.short_description = 'Phone number'
