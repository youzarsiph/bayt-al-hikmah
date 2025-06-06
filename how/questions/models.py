"""Data Models for how.questions"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable

from how.mixins.models import DateTimeMixin
from how.questions import QUESTION_TYPES


# Create your models here.
User = get_user_model()


class Question(DateTimeMixin, Orderable, ClusterableModel, models.Model):
    """Assignment Questions"""

    assignment = ParentalKey(
        "assignments.Assignment",
        on_delete=models.CASCADE,
        related_name="questions",
        help_text=_("Question assignment"),
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        choices=QUESTION_TYPES,
        help_text=_("Question type"),
    )
    text = RichTextField(help_text=_("Question text"))

    # Dashboard UI config
    panels = [
        FieldPanel("type"),
        FieldPanel("text"),
        InlinePanel("answers", heading="Answers", label="Answer"),
    ]

    def __str__(self) -> str:
        return f"{self.assignment}: Question {self.sort_order}"
