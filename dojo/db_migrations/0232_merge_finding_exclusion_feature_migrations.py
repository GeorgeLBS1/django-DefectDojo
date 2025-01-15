# Generated by Django 5.0.9 on 2025-01-13 21:36

import django.db.models.deletion
import multiselectfield.db.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0231_system_settings_enforce_verified_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='finding',
            name='priority',
            field=models.FloatField(blank=True, default=0.0, null=True),
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
            model_name='finding',
            name='risk_status',
            field=models.CharField(choices=[('Risk Pending', 'Risk Pending'), ('Risk Rejected', 'Risk Rejected'), ('Risk Expired', 'Risk Expired'), ('Risk Accepted', 'Risk Accepted'), ('Risk Active', 'Risk Active'), ('On Whitelist', 'On Whitelist'), ('On Blacklist', 'On Blacklist'), ('Transfer Pending', 'Transfer Pending'), ('Transfer Rejected', 'Transfer Rejected'), ('Transfer Expired', 'Transfer Expired'), ('Transfer Accepted', 'Transfer Accepted')], default='Risk Active', help_text='Denotes the type of finding status, (pending, rejected).', max_length=20, null=True, verbose_name='Risk Status'),
        ),
        migrations.CreateModel(
            name='FindingExclusion',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('white_list', 'white_list'), ('black_list', 'black_list')], max_length=12)),
                ('unique_id_from_tool', models.CharField(blank=True, help_text='Vulnerability technical id from the source tool. Allows to track unique vulnerabilities.', max_length=500, verbose_name='Vulnerability Id')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('notification_sent', models.BooleanField(default=False)),
                ('expiration_date', models.DateTimeField(null=True)),
                ('last_status_update', models.DateTimeField(auto_now=True)),
                ('status_updated_at', models.DateTimeField(null=True)),
                ('reviewed_at', models.DateTimeField(blank=True, null=True)),
                ('reason', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Rejected', 'Rejected'), ('Expired', 'Expired')], default='Pending', max_length=8)),
                ('final_status', models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dojo_user_created', to='dojo.dojo_user')),
                ('status_updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dojo_user_status_updated', to='dojo.dojo_user')),
            ],
            options={
                'db_table': 'dojo_finding_exlusion',
            },
        ),
        migrations.CreateModel(
            name='FindingExclusionDiscussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dojo.dojo_user')),
                ('finding_exclusion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to='dojo.findingexclusion')),
            ],
            options={
                'db_table': 'dojo_finding_exclusion_discussion',
            },
        ),
    ]