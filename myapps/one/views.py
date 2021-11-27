from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from myapps.one.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import authentication
from rest_framework.permissions import AllowAny
from myapps.one.serializers import MyTokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
from helpers import Json
import json as j
    

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

    def post(self, request, *args, **kwargs):
        datas = j.loads(request.body.decode('utf-8'))
        if 'email' not in datas:
            return Json.errorResponse('email is Required', 400)
        else:
            email = datas['email']
        if 'password' not in datas:
            return Json.errorResponse('Password is Required',400)
        else:
            password = datas['password']
        
        try:
            login_user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Json.errorResponse('Please enter the valid email', 401)

        if not login_user.is_active:  # for inactive users
            return Json.errorResponse('Your account has been blocked by admin,Please contact admin', 401)

        if check_password(datas['password'], login_user.password):
            response = "Invalid credentials"
            user = CustomUser.objects.filter(email=email, password=password)

            if (user != None):
                serializer = self.get_serializer(data=request.data)
                response = serializer.validate(request.data)
            else:
                return Json.errorResponse(response, 401)

            return Json.successResponse("Login successfully",response,200)


        return Json.errorResponse('Incorrect password', 401)
        last_login = Profile.objects.filter(id=request.user.id).update(last_login=timezone.now())
