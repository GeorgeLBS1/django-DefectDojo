# Generated by Django 5.0.9 on 2024-12-06 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0231_findingexclusion_reviewed_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='findingexclusion',
            name='final_status',
            field=models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected')], null=True),
        ),
    ]
