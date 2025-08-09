# accounts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignUpViewSet

router = DefaultRouter()
router.register(r"", SignUpViewSet, basename="signup")

urlpatterns = [
    path("", include(router.urls)),
]
