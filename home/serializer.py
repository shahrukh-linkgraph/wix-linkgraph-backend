from .models import *
from rest_framework.serializers import ModelSerializer



class WixSerializer(ModelSerializer):
    class Meta:
        model = Wix
        fields = "__all__"