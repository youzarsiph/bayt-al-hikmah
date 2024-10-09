""" Data Models for bayt_al_hikmah.courses """

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Course(models.Model):
    """Courses"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Instructor",
    )
    path = models.ForeignKey(
        "paths.Path",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Learning path",
    )
    image = models.ImageField(
        help_text="Image",
        upload_to="images/courses/",
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
        help_text="Designates if the course is approved",
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
