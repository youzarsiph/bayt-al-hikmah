""" API endpoints for bayt_al_hikmah.departments """

from typing import Any, List
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from bayt_al_hikmah.departments.models import Department
from bayt_al_hikmah.departments.serializers import DepartmentSerializer


# Create your views here.
class DepartmentViewSet(ModelViewSet):
    """Create, view, update and delete Departments"""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "headline", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["faculty", "name"]

    def get_permissions(self) -> List[Any]:
        if self.action not in ["list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()
