"""Data Models for how.categories"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index

from how.mixins.models import DateTimeMixin


# Create your models here.
class Category(DateTimeMixin, Page):
    """Categories"""

    description = RichTextField(help_text=_("Category description"))

    # Dashboard UI config
    show_in_menus = True
    context_object_name = "category"
    template = "ui/previews/category.html"
    content_panels = Page.content_panels + [FieldPanel("description")]
    page_description = _(
        "Categories help organize courses into thematic or subject-related groupings, "
        "making it easier for users to explore and filter available courses."
    )

    # Search fields
    search_fields = Page.search_fields + [index.SearchField("description")]

    # API fields
    api_fields = [APIField("description")]

    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["courses.Course", "paths.LearningPath"]

    class Meta:
        """Meta data"""

        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.title
