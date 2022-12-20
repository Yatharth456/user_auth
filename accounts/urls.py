from django.contrib import admin
from django.urls import path
from accounts.views import (
    LoginAPI, RegisterAPI, ProfileAPI, AddressAPI, AllProfileAPI, managerAPI
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('login/2/', TokenObtainPairView.as_view(), name='login2'),
    path('profile/', ProfileAPI.as_view(), name='profile'),
    path('address/', AddressAPI.as_view(), name='address'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('manager/', managerAPI.as_view(), name='manager' ),
    path('all-profile/', AllProfileAPI.as_view(), name='profile'),
]