# nominations_awards/views.py

from rest_framework import viewsets, permissions, filters
from .models import Nomination
from .serializers import NominationSerializer

class NominationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows:
      - Anyone to list all nominations (approved or not)
      - Anyone to create a new nomination
      - Anyone to retrieve a single nomination
      - (Later) Only admins can update or delete
    For now, permission_classes = [AllowAny].
    """
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "nominee_name",
        "nominee_email",
        "nominee_institution",
        "nominated_by_name",
        "nominated_by_email",
        "category",
    ]
    ordering_fields = ["submitted_at", "nominee_name", "category"]

    def get_queryset(self):
        """
        By default, show all nominations. If you want the frontend to show only
        approved ones, you could filter: Nomination.objects.filter(approved=True).
        For now, return everything (the frontend can filter out unapproved if desired).
        """
        return Nomination.objects.all().order_by("-submitted_at")
