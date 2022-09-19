from drf_model_perm_app.models import Tool
from rest_framework import serializers


class ToolSerializer(serializers.ModelSerializer):
    """ Tool serializer """

    class Meta:
        """ Meta """
        model = Tool
        fields = '__all__'