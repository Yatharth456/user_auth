from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from accounts.models import User, Profile, Address
from django.contrib.auth.decorators import login_required

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all().select_related('User').select_related('Profile').select_related('Address')

    def get(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
    @login_required
    def user(request):
        return render(request)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class AddressAPI(generics.GenericAPIView):
    SERIALIZER = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        addresses = Address.objects.all()
        return Response({"address": addresses})

class ProfileAPI(generics.GenericAPIView):
    SERIALIZER = RegisterSerializer

    def get(self, request, *args, **kwargs):
       profiles = Profile.objects.all()
       return Response({"profile": profiles})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        profiles = Profile.objects.all()
        return Response({"profile": profiles})
        serializer.save()