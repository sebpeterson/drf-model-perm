from django.shortcuts import render
from drf_model_perm_app.models import Tool
from drf_model_perm_app.serializers import ToolSerializer

from rest_framework import status, viewsets
from rest_framework.permissions import DjangoModelPermissions

# Create your views here.
class ToolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [DjangoModelPermissions]
    
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
