from .models import *
from rest_framework.serializers import ModelSerializer


class JobAddSerializer(ModelSerializer):
    class Meta:
        model = JobAdd
        fields = '__all__'