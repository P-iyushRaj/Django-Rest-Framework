"""gs24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

]

from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView

router = DefaultRouter()

#register viewset using router
# url http://127.0.0.1:8000/studentapi
router.register('studentapi', views.StudentModelViewSet,
basename='Student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    #path('gettoken/', obtain_auth_token),
    #http POST http://127.0.0.1:8000/gettoken/ username="normal" password="hreya@123"
    #will generate token

    #path('gettokenand/', CustomAuthToken.as_view())
    path('gettoken/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #http POST http://127.0.0.1:8000/gettoken/ username="piyush" password="123456"
    path('refreshtoken/',TokenRefreshView.as_view(), name='token_refresh'),
    #http POST http://127.0.0.1:8000/refreshtoken/ refresh"refresh token here"
    path('verifytoken/',TokenVerifyView.as_view(), name='token_verify'),
    #http POST http://127.0.0.1:8000/verifytoken/ token="eyJ0e"

]

#token valid for 5min
#refreshtoken valid for 1day
