# Generated by Django 4.1.13 on 2024-04-26 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0212_system_settings_filter_string_matching'),
    ]

    operations = [
        migrations.AddField(
            model_name='system_settings',
            name='enable_similar_findings',
            field=models.BooleanField(default=True, help_text='Enable the query of similar findings on the view finding page. This feature can involve potentially large queries and negatively impact performance', verbose_name='Enable Similar Findings'),
        ),
    ]
