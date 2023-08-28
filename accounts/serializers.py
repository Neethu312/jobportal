from rest_framework.serializers import ModelSerializer
from .models import *


class CustomUserSerializer(ModelSerializer):

    def save(self, **kwargs):
        account = super().save(**kwargs)
        account.set_password(self.validated_data.get('password'))
        account.is_active = True
        account.save()
        return account

    class Meta:
        model = CustomUser
        fields = '__all__'


class CompanyProfileSerializer(ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'


class ApplicantProfileSerializer(ModelSerializer):
    class Meta:
        model = ApplicantProfile
        fields = '__all__'
