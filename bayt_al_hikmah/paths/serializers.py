""" Serializers for bayt_al_hikmah.paths """

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.paths.models import Path


# Create your serializers here.
class PathSerializer(ModelSerializer):
    """Specialization serializer"""

    class Meta:
        """Meta data"""

        model = Path
        read_only_fields = ["institute", "is_approved"]
        fields = [
            "id",
            "url",
            "institute",
            "instructors",
            "image",
            "name",
            "headline",
            "description",
            "is_approved",
            "created_at",
            "updated_at",
        ]
