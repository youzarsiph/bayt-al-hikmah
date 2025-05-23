"""Serializers for bayt_al_hikmah.questions"""

from rest_framework.serializers import ModelSerializer

from bayt_al_hikmah.questions.models import Question


# Create your serializers here.
class QuestionSerializer(ModelSerializer):
    """Question serializer"""

    class Meta:
        """Meta data"""

        model = Question
        read_only_fields = ["assignment"]
        fields = [
            "id",
            "url",
            "assignment",
            "type",
            "text",
            "created_at",
            "updated_at",
        ]
