# Generated by Django 4.1.11 on 2023-11-12 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0193_notifications_scan_added_empty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system_settings',
            name='enable_auditlog',
        ),
    ]
