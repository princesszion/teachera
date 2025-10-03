# opportunities/views.py

from rest_framework import viewsets, filters, permissions

from opportunities.pagination import StandardResultsSetPagination
from .models import Category, Opportunity
from .serializers import CategorySerializer, OpportunitySerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

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
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request  # ✅ gives mixin access to build_absolute_uri
        return context
    def get_queryset(self):
        return Opportunity.objects.filter(is_active=True).order_by("-post_date")

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all().order_by('-post_date')
    serializer_class = OpportunitySerializer
    permission_classes = [permissions.AllowAny]