from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from . models import CustomUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  def get(self,request,*args,**kwargs):
    print(request.user.id,'abc')
    user = CustomUser.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=200)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer