# Generated by Django 4.2.15 on 2024-09-22 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dojo", "0224_test_type_dynamically_generated"),
    ]

    operations = [
        migrations.CreateModel(
            name="FindingExclusion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("white_list", "white_list"),
                            ("black_list", "black_list"),
                        ],
                        max_length=12,
                    ),
                ),
                (
                    "unique_id_from_tool",
                    models.CharField(
                        blank=True,
                        help_text="Vulnerability technical id from the source tool. Allows to track unique vulnerabilities.",
                        max_length=500,
                        verbose_name="Unique ID from tool",
                    ),
                ),
                ("create_date", models.DateTimeField(auto_now=True)),
                ("expiration_date", models.DateTimeField()),
                ("user_history", models.IntegerField(null=True)),
                ("reason", models.CharField(blank=True, max_length=200)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Accepted", "Accepted"),
                            ("Pending", "Pending"),
                            ("Rejected", "Rejected"),
                        ],
                        max_length=8,
                    ),
                ),
                (
                    "accepted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dojo.dojo_user",
                    ),
                ),
                (
                    "finding",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dojo.finding",
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dojo.product",
                    ),
                ),
            ],
            options={
                "db_table": "dojo_finding_exlusion",
            },
        ),
    ]
