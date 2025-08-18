# opportunities/views.py

from rest_framework import viewsets, filters, permissions

from opportunities.pagination import StandardResultsSetPagination
from .models import Category, Opportunity
from .serializers import CategorySerializer, OpportunitySerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

@method_decorator(csrf_exempt, name='dispatch')
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category (e.g. Jobs, Scholarships) to be
    listed, retrieved, created, updated, and deleted by anyone.
    """
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  # public access

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.filter(is_active=True).order_by("-post_date")
    serializer_class = OpportunitySerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination  # 👈 Add this line

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description", "location"]
    ordering_fields = ["post_date", "title"]

    def get_queryset(self):
        return Opportunity.objects.filter(is_active=True).order_by("-post_date")

# class OpportunityViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows Opportunity to be listed, retrieved,
#     created, updated, and deleted by anyone.
#     """
#     queryset = Opportunity.objects.filter(is_active=True).order_by("-post_date")
#     serializer_class = OpportunitySerializer
#     permission_classes = [permissions.AllowAny]  # public access

#     # You can search/filter in–house if desired
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ["title", "description", "location"]
#     ordering_fields = ["post_date", "title"]

#     def get_queryset(self):
#         """
#         By default, return only active opportunities.
#         If you want to let clients see inactive ones as well,
#         comment out the filter(is_active=True) line.
#         """
#         return Opportunity.objects.filter(is_active=True).order_by("-post_date")
