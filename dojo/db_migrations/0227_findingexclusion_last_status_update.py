# Generated by Django 5.0.9 on 2024-11-19 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0226_rename_producto_findingexclusion_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='findingexclusion',
            name='last_status_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
