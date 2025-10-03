# # opportunities/serializers.py

# from rest_framework import serializers
# from .models import Category, Opportunity
# from common.serializers import AbsoluteMediaURLMixin
# from django.utils import timezone 
# class CategorySerializer(AbsoluteMediaURLMixin,serializers.ModelSerializer):
#     """
#     Read/write serializer for Category.
#     """
#     class Meta:
#         model = Category
#         fields = ["id", "name", "slug"]


# class OpportunitySerializer(AbsoluteMediaURLMixin, serializers.ModelSerializer):
#     is_closed = serializers.SerializerMethodField() 
#     """
#     Read/write serializer for Opportunity.
#     - Includes nested Category (read-only) and a write-only field category_id.
#     """
#     category = CategorySerializer(read_only=True)
#     category_id = serializers.PrimaryKeyRelatedField(
#         queryset=Category.objects.all(),
#         source="category",
#         write_only=True,
#         help_text="ID of an existing Category"
#     )

#     class Meta:
#         model = Opportunity
#         fields = [
#             "id",
#             "title",
#             "description",
#             "organization",
#             "deadline", 
#             "post_date",
#             "category",
#             "category_id",
#             "eligibility",
#             "benefits",
#             "process",
#             "location",
#             "is_active",
#             "is_closed",
#         ]
#         read_only_fields = ["post_date"]
#     def get_is_closed(self, obj):
#         return obj.deadline < timezone.now()

from rest_framework import serializers
from django.utils import timezone
from .models import Opportunity, Category
from common.serializers import AbsoluteMediaURLMixin  # ✅ import mixin

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class OpportunitySerializer(AbsoluteMediaURLMixin, serializers.ModelSerializer):
    is_closed = serializers.SerializerMethodField()

    class Meta:
        model = Opportunity
        fields = "__all__"

    def get_is_closed(self, obj):
        if obj.deadline:
            return obj.deadline < timezone.now()
        return False
