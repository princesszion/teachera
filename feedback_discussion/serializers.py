# feedback_discussion/serializers.py

from rest_framework import serializers
from .models import Feedback, DiscussionComment

class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for Feedback:
      - name and email are optional
      - content is required
      - created_at is read-only
    """
    class Meta:
        model = Feedback
        fields = ["id", "name", "email", "content", "created_at"]
        read_only_fields = ["id", "created_at"]


class DiscussionCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for DiscussionComment:
      - includes nested replies (read-only)
      - accepts parent ID (if this comment is a reply)
      - name and email optional
      - body required
      - created_at read-only
    """
    # Nested replies (each reply will be serialized recursively)
    replies = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DiscussionComment
        fields = [
            "id",
            "name",
            "email",
            "body",
            "parent",
            "replies",
            "created_at",
        ]
        read_only_fields = ["id", "replies", "created_at"]

    def get_replies(self, obj):
        """
        Recursively serialize children (replies).
        """
        if obj.replies.exists():
            return DiscussionCommentSerializer(
                obj.replies.all().order_by("created_at"), many=True
            ).data
        return []
