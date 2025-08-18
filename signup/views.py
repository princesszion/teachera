# accounts/views.py
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import SignupSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

@method_decorator(csrf_exempt, name='dispatch')
class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # ✅ Required for ModelViewSet
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]
