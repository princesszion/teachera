# resources/serializers.py

from rest_framework import serializers
from .models import Resource, ResourcePurchase

class ResourceSerializer(serializers.ModelSerializer):
    """
    Serializer for Resource model:
    - file → will show a URL to download
    """
    file_url = serializers.FileField(source="file", read_only=True)

    class Meta:
        model = Resource
        fields = [
            "id",
            "title",
            "description",
            "file_url",
            "price",
            "uploader_name",
            "uploader_email",
            "created_at",
        ]
        read_only_fields = ["created_at", "file_url"]

    def create(self, validated_data):
        """
        Handle file upload properly. The instance ID isn't available until after save(),
        so we override create() to save first, then re-save file to get correct path.
        """
        uploaded_file = validated_data.pop("file", None)
        # Create the Resource object without the file (so we get an ID)
        resource = Resource.objects.create(**validated_data)
        if uploaded_file:
            resource.file = uploaded_file
            resource.save()
        return resource


class ResourcePurchaseSerializer(serializers.ModelSerializer):
    """
    Serializer for ResourcePurchase. Exposes resource ID and buyer info.
    """
    resource_id = serializers.PrimaryKeyRelatedField(
        queryset=Resource.objects.all(),
        source="resource",
        write_only=True,
        help_text="ID of resource being purchased"
    )
    resource = ResourceSerializer(read_only=True)

    class Meta:
        model = ResourcePurchase
        fields = [
            "id",
            "resource",
            "resource_id",
            "buyer_name",
            "buyer_email",
            "purchased_at",
            "transaction_id",
        ]
        read_only_fields = ["purchased_at", "resource"]
