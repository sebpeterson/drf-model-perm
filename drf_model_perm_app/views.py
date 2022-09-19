import copy

from django.shortcuts import render
from drf_model_perm_app.models import Tool
from drf_model_perm_app.serializers import ToolSerializer

from rest_framework import status, viewsets
from rest_framework.permissions import DjangoModelPermissions

# Create your views here.

class CustomDjangoModelPermission(DjangoModelPermissions):
    """"
    https://stackoverflow.com/questions/46584653/django-rest-framework-use-djangomodelpermissions-on-listapiview
    """
    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

class ToolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [CustomDjangoModelPermission]
    
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
