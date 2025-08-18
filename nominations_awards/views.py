# # nominations_awards/views.py

# from rest_framework import viewsets, permissions, filters
# from .models import Nomination
# from .serializers import NominationSerializer

# class NominationViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows:
#       - Anyone to list all nominations (approved or not)
#       - Anyone to create a new nomination
#       - Anyone to retrieve a single nomination
#       - (Later) Only admins can update or delete
#     For now, permission_classes = [AllowAny].
#     """
#     queryset = Nomination.objects.all()
#     serializer_class = NominationSerializer
#     permission_classes = [permissions.AllowAny]

#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = [
#         "nominee_name",
#         "nominee_email",
#         "nominee_institution",
#         "nominated_by_name",
#         "nominated_by_email",
#         "category",
#     ]
#     ordering_fields = ["submitted_at", "nominee_name", "category"]

#     def get_queryset(self):
#         """
#         By default, show all nominations. If you want the frontend to show only
#         approved ones, you could filter: Nomination.objects.filter(approved=True).
#         For now, return everything (the frontend can filter out unapproved if desired).
#         """
#         return Nomination.objects.all().order_by("-submitted_at")

from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend  # ✅ Add this
from .models import Nomination
from .serializers import NominationSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

@method_decorator(csrf_exempt, name='dispatch')
class NominationViewSet(viewsets.ModelViewSet):
    queryset = Nomination.objects.all().order_by("-submitted_at")
    serializer_class = NominationSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # ✅ Add DjangoFilterBackend
    filterset_fields = ["approved", "category"]  # ✅ Enable filtering by these fields

    search_fields = [
        "nominee_name",
        "nominee_email",
        "nominee_institution",
        "nominated_by_name",
        "nominated_by_email",
        "category",
    ]
    ordering_fields = ["submitted_at", "nominee_name", "category"]
