from django.http import response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from helpers import Json
from helpers.common import get_user_role
from rest_framework import serializers

from myapps.one.models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['role'] = get_user_role(self.user)
        data['last_login'] = str(self.user.last_login)[:16]

        return data

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =('id','email',)
