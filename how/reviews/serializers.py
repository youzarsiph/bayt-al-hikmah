"""Serializers for how.reviews"""

from rest_framework.serializers import ModelSerializer

from how.reviews.models import Review


# Create your serializers here.
class ReviewSerializer(ModelSerializer):
    """Review serializer"""

    class Meta:
        """Meta data"""

        model = Review
        read_only_fields = ["owner", "course", "sentiment"]
        fields = [
            "id",
            "url",
            "owner",
            "course",
            "rating",
            "comment",
            "sentiment",
            "created_at",
            "updated_at",
        ]
