# resources/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import ResourceViewSet, ResourcePurchaseViewSet

router = routers.DefaultRouter()
router.register(r"resources", ResourceViewSet, basename="resource")
router.register(r"purchases", ResourcePurchaseViewSet, basename="purchase")

urlpatterns = [
    path("", include(router.urls)),
]
