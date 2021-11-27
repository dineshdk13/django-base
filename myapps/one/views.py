from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from myapps.one.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import authentication
from rest_framework.permissions import AllowAny
from myapps.one.serializers import MyTokenObtainPairSerializer

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {
        'message': "Hi,dinesh Welcom",
    }
    return HttpResponse(template.render(context, request))


class MyObtainTokenPairView(TokenObtainPairView):
    authentication_classes  = [authentication.JWTTokenUserAuthentication]
    serializer_class        = MyTokenObtainPairSerializer
    permission_classes      = (AllowAny,)
    queryset                = CustomUser.objects.all()
