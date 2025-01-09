# Generated by Django 5.1 on 2025-01-01 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Specialization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Specialization image",
                        upload_to="images/specializations/",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, help_text="Specialization name", max_length=64
                    ),
                ),
                (
                    "headline",
                    models.CharField(
                        db_index=True,
                        help_text="Specialization headline",
                        max_length=128,
                    ),
                ),
                (
                    "description",
                    models.TextField(help_text="Specialization description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="Date created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Last update"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="Specialization category",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specializations",
                        to="categories.category",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        help_text="Specialization department",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="specializations",
                        to="departments.department",
                    ),
                ),
            ],
        ),
    ]
