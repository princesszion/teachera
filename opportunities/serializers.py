# opportunities/serializers.py

from rest_framework import serializers
from .models import Category, Opportunity

class CategorySerializer(serializers.ModelSerializer):
    """
    Read/write serializer for Category.
    """
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class OpportunitySerializer(serializers.ModelSerializer):
    """
    Read/write serializer for Opportunity.
    - Includes nested Category (read-only) and a write-only field category_id.
    """
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        help_text="ID of an existing Category"
    )

    class Meta:
        model = Opportunity
        fields = [
            "id",
            "title",
            "description",
            "post_date",
            "category",
            "category_id",
            "opportunity_type",
            "location",
            "is_active",
        ]
        read_only_fields = ["post_date"]
