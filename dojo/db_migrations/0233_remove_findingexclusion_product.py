# Generated by Django 5.0.9 on 2025-01-03 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0232_remove_findingexclusion_accepted_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='findingexclusion',
            name='product',
        ),
    ]
