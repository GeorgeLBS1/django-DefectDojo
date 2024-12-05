# Generated by Django 5.0.9 on 2024-11-28 19:40

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0228_component_finding_component'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='risk_acceptance_confirmed',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('slack', 'slack'), ('msteams', 'msteams'), ('mail', 'mail'), ('webhooks', 'webhooks'), ('alert', 'alert')], default=('mail', 'alert'), help_text='Send notification to confirm acceptance process', max_length=33, verbose_name='Risk Acceptance Confirmed'),
        ),
    ]
