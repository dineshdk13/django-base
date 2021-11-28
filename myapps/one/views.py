from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from myapps.one.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import authentication
from rest_framework.permissions import AllowAny,SAFE_METHODS,BasePermission
from myapps.one.serializers import MyTokenObtainPairSerializer,CustomUserSerializer
from django.contrib.auth.hashers import check_password
from helpers import Json
import json as j
from django.utils import timezone
from helpers.common import get_user_role


# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {
        'message': "Hi,dinesh Welcom",
    }
    return HttpResponse(template.render(context, request))

class AsSuperAsminPermission(BasePermission):
    message="Super admin can only access this api"

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        print(get_user_role(request.user),"test")
        return get_user_role(request.user) == 'User'

    # def has_object_permission(self, request, view, obj):
    #     """
    #     Return `True` if permission is granted, `False` otherwise.
    #     """
    #     return obj.CustomUser == request.user


class MyObtainTokenPairView(TokenObtainPairView):
    authentication_classes = [authentication.JWTTokenUserAuthentication]
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            datas = j.loads(request.body.decode('utf-8'))
            if 'email' not in datas:
                return Json.errorResponse('email is Required', 400)
            else:
                email = datas['email']
            if 'password' not in datas:
                return Json.errorResponse('Password is Required', 400)
            else:
                password = datas['password']

            try:
                login_user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Json.errorResponse('Please enter the valid email', 401)

            if not login_user.is_active:  # for inactive users
                return Json.errorResponse('Your account has been blocked by admin,Please contact admin', 401)

            if check_password(password, login_user.password):
                serializer = self.get_serializer(data=request.data)
                response = serializer.validate(request.data)

                #update last_login
                login_user.last_login = timezone.now()
                login_user.save()
                return Json.successResponse("Login successfully", response, 200)

            return Json.errorResponse('Incorrect password', 401)
        except Exception as e:
            print(e)
            return Json.errorResponse('Something went wrong. Please try again after sometime', 401)


class Test (APIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AsSuperAsminPermission]
    queryset = CustomUser.objects.all()
    def post(self,request):
        serializer=self.serializer_class(request.user).data
        return Json.successResponse("Welcome superadmin", serializer, 200)

