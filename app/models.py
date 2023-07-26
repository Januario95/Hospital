from django.db import models

from ._helpers import PRIORITY

class Patient(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number
        }

    class Meta:
        ordering = ('first_name',)
        unique_together = ('first_name', 'last_name',
                           'phone_number')

class Appointment(models.Model):
    patient = models.ForeignKey(
        to=Patient,
        on_delete=models.CASCADE
    )
    disease = models.CharField(max_length=50)
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY,
        default='Nao Urgente'
    )
    completed = models.BooleanField(default=False)
    # description = models.CharField(max_length=255)
    date = models.DateField()
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient} - {self.disease}'
    
    def serialize(self):
        return {
            'id': self.pk,
            'patient': self.patient.serialize(),
            'disease': self.disease,
            'priority': self.priority,
            'completed': self.completed,
            'date': self.date,
            'entry_date': self.entry_date
        }