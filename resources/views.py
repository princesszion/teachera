# resources/views.py

from rest_framework import viewsets, permissions, filters
from .models import Resource, ResourcePurchase
from .serializers import ResourceSerializer, ResourcePurchaseSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing, retrieving, creating, updating, and deleting Resources.
    """
    queryset = Resource.objects.all().order_by("-created_at")
    serializer_class = ResourceSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description", "uploader_name"]
    ordering_fields = ["created_at", "price", "title"]


class ResourcePurchaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and creating ResourcePurchases.
    """
    queryset = ResourcePurchase.objects.all().order_by("-purchased_at")
    serializer_class = ResourcePurchaseSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["buyer_name", "buyer_email", "resource__title"]
    ordering_fields = ["purchased_at"]
