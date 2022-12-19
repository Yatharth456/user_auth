from django.shortcuts import render
# Create your views here.
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserListSerializer, RegisterSerializer, ProfileSerializer, AddressSerializer
from accounts.models import CustomUser, Profile, Address
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from accounts.decorators import IsAdmin, IsEmployee, IsManager

class LoginAPI(APIView):

    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        
        data = {
            'role': user.role,
            'email': user.email,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data, status=200)

    @login_required
    def user(request):
        return render(request)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    #permission_classes = (permissions.AllowAny,)


    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class AddressAPI(generics.GenericAPIView):
    serializer_class = AddressSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"address": serializer.data})
class ProfileAPI(generics.GenericAPIView):
    serializer_class= ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def post(self, request, *args, **kwargs):
        data = request.data
        data["users"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"profile": serializer.data})