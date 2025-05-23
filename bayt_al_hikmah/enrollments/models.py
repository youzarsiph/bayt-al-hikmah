"""Data Models for bayt_al_hikmah.enrollments"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from bayt_al_hikmah.enrollments import ENROLLMENT_ROLES
from bayt_al_hikmah.mixins.models import DateTimeMixin


# Create your models here.
User = get_user_model()


class Enrollment(DateTimeMixin, models.Model):
    """Course Enrollments"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments",
        help_text=_("Enrolling User"),
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="enrollments",
        help_text=_("Enrolled Course"),
    )
    role = models.PositiveSmallIntegerField(
        default=0,
        choices=ENROLLMENT_ROLES,
        help_text=_("Enrollment role"),
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_course_enrollment",
                fields=["user", "course"],
            )
        ]

    def __str__(self) -> str:
        return f"{self.user}-{self.course}-{ENROLLMENT_ROLES[self.role][1]}"
