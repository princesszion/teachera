# nominations_awards/serializers.py

from rest_framework import serializers
from .models import Nomination
from common.serializers import AbsoluteMediaURLMixin

class NominationSerializer(AbsoluteMediaURLMixin, serializers.ModelSerializer):
    """
    Serializer for Nomination:
      - Exposes all fields.
      - 'submitted_at' is read-only.
      - 'approved' is writeable (so admin endpoints can toggle it).
    """
    class Meta:
        model = Nomination
        fields = [
            "id",
            "nominee_name",
            "nominee_email",
            "nominee_institution",
            "category",
            "rationale",
            "nominated_by_name",
            "nominated_by_email",
            "submitted_at",
            "approved",
            "photo",
        ]
        read_only_fields = ["id", "submitted_at"]
