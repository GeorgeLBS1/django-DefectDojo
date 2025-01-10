# Generated by Django 5.0.9 on 2025-01-10 01:11

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0231_finding_priority_alter_finding_risk_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='findingexclusion',
            name='accepted_by',
        ),
        migrations.RemoveField(
            model_name='findingexclusion',
            name='finding',
        ),
        migrations.RemoveField(
            model_name='findingexclusion',
            name='product',
        ),
        migrations.RemoveField(
            model_name='findingexclusion',
            name='user_history',
        ),
        migrations.AddField(
            model_name='notifications',
            name='finding_exclusion_approved',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('slack', 'slack'), ('msteams', 'msteams'), ('mail', 'mail'), ('webhooks', 'webhooks'), ('alert', 'alert')], default=('alert', 'alert'), help_text='Get notified of finding exclusion requests approved', max_length=33, verbose_name='Finding exclusion approved'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='finding_exclusion_expired',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('slack', 'slack'), ('msteams', 'msteams'), ('mail', 'mail'), ('webhooks', 'webhooks'), ('alert', 'alert')], default=('alert', 'alert'), help_text='Get notified of finding exclusion requests expired', max_length=33, verbose_name='Finding exclusion expired'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='finding_exclusion_rejected',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('slack', 'slack'), ('msteams', 'msteams'), ('mail', 'mail'), ('webhooks', 'webhooks'), ('alert', 'alert')], default=('alert', 'alert'), help_text='Get notified of finding exclusion requests rejected', max_length=33, verbose_name='Finding exclusion rejected'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='finding_exclusion_request',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('slack', 'slack'), ('msteams', 'msteams'), ('mail', 'mail'), ('webhooks', 'webhooks'), ('alert', 'alert')], default=('alert', 'alert'), help_text='Get notified of finding exclusion requests', max_length=33, verbose_name='Finding exclusion request'),
        ),
        migrations.AlterField(
            model_name='findingexclusion',
            name='final_status',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], null=True),
        ),
        migrations.AlterField(
            model_name='findingexclusion',
            name='status',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Rejected', 'Rejected'), ('Expired', 'Expired')], default='Pending', max_length=8),
        ),
        migrations.AlterField(
            model_name='findingexclusion',
            name='unique_id_from_tool',
            field=models.CharField(blank=True, help_text='Vulnerability technical id from the source tool. Allows to track unique vulnerabilities.', max_length=500, verbose_name='Vulnerability Id'),
        ),
    ]
