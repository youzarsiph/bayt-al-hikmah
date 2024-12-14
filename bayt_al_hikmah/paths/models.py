""" Data Models for bayt_al_hikmah.paths """

from django.db import models


# Create your models here.
class Path(models.Model):
    """Learning paths, collections of related courses"""

    institute = models.ForeignKey(
        "institutes.Institute",
        on_delete=models.CASCADE,
        related_name="paths",
        help_text="Institute",
    )
    instructors = models.ManyToManyField(
        "instructors.Instructor",
        help_text="Instructors",
    )
    image = models.ImageField(
        help_text="Image",
        upload_to="images/paths/",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Name",
    )
    headline = models.CharField(
        max_length=128,
        db_index=True,
        help_text="Headline",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Description",
    )
    is_approved = models.BooleanField(
        default=False,
        help_text="Designates if the path is approved",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return self.name
