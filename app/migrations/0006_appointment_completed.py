# Generated by Django 4.2.1 on 2023-05-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_appointment_description_appointment_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
