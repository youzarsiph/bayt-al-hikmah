# Generated by Django 5.1 on 2025-01-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
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
                    "is_correct",
                    models.BooleanField(
                        default=False, help_text="Weather the answer is correct"
                    ),
                ),
                ("text", models.CharField(help_text="Answer text", max_length=64)),
                (
                    "description",
                    models.CharField(
                        help_text="Why the answer is correct or wrong", max_length=512
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="Date created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Last update"),
                ),
            ],
        ),
    ]
