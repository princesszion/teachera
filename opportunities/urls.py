# opportunities/urls.py

from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet, OpportunityViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"opportunities", OpportunityViewSet, basename="opportunity")

urlpatterns = [
    path("", include(router.urls)),
]
