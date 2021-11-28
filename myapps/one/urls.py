from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('template', views.index, name='index'),
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test', views.Test.as_view(), name='test'),

]