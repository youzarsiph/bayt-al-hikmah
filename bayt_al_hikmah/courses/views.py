""" API endpoints for bayt_al_hikmah.courses """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from bayt_al_hikmah.mixins import OwnerMixin
from bayt_al_hikmah.courses.models import Course
from bayt_al_hikmah.courses.serializers import CourseSerializer


# Create your views here.
class CourseViewSet(OwnerMixin, ModelViewSet):
    """Create, view, update and delete Courses"""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["name", "created_at", "updated_at"]
    filterset_fields = ["path", "name", "is_approved"]
