"""Data Models for how.users"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    """Users"""

    is_instructor = models.BooleanField(
        null=True,
        blank=True,
        help_text=_("Designates weather the user is an instructor"),
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text=_("Profile image"),
        upload_to="images/users/",
    )
    bio = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=_("Tell us about yourself"),
    )
    # NOTE: When generating migrations, you need to comment this field
    # generate the migrations then uncomment it to add it to Item model
    # to avoid django.db.migrations.exceptions.CircularDependencyError
    # saved = models.ManyToManyField(
    #     "paths.LearningPath",
    #     related_name="savers",
    #     help_text=_("Saved learning paths"),
    # )
    # items = models.ManyToManyField(
    #     "items.Item",
    #     related_name="completers",
    #     help_text=_("Completed items"),
    # )
