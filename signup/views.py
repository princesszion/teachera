# accounts/views.py
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import SignupSerializer

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # ✅ Required for ModelViewSet
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
