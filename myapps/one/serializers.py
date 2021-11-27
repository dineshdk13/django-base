from django.http import response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from helpers import Json


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
        data['is_superuser'] = self.user.is_superuser
        response={}
        response['status'] = 'OK'
        response['message'] = 'Login successfully'
        response['data'] = data
        

        return response