# Generated by Django 5.0.8 on 2024-09-04 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0222_system_settings_enable_ui_table_based_searching'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_type',
            name='dynamically_generated',
            field=models.BooleanField(default=False, help_text='Set to True for test types that are created at import time'),
        ),
    ]
