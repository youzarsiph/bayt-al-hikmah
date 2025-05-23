"""Data Models for bayt_al_hikmah.reviews"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from bayt_al_hikmah.mixins.models import DateTimeMixin
from bayt_al_hikmah.reviews import RATINGS


# Create your models here.
User = get_user_model()


class Review(DateTimeMixin, models.Model):
    """Course Reviews"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        help_text=_("Reviewer"),
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="reviews",
        help_text=_("Reviewed course"),
    )
    rating = models.PositiveSmallIntegerField(
        default=1,
        choices=RATINGS,
        help_text=_("Review rating"),
    )
    comment = models.CharField(
        max_length=512,
        db_index=True,
        help_text=_("Review comment"),
    )
    sentiment = models.BooleanField(
        null=True,
        blank=True,
        help_text=_("Review sentiment"),
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(name="unique_review", fields=["user", "course"])
        ]

    def __str__(self) -> str:
        return f"{self.user}: {self.course}-{self.rating}"
