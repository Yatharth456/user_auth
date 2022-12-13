from django.shortcuts import render
# Create your views here.
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, ProfileSerializer, AddressSerializer
from accounts.models import CustomUser, Profile, Address
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPI(APIView):
    permission_classes = (permissions.AllowAny,)
   
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        data = {
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

    def post(self, request, *args, **kwargs):
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
    permission_classes = [permissions.IsAuthenticated,]

    # def get(self, request, *args, **kwargs):
    #    profiles = Profile.objects.all()
    #    return Response({"profile": request.data}) #check

    def post(self, request, *args, **kwargs):
        data = request.data
        data["users"] = request.user.id
        print(data)
        
        #users = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"profile": serializer.data})
        #return Response({'id': request.user.id})
        # print(request.data)
        # data = request.data
        # params = request.query_params
        # params = request.GET
        # id = params['id']
        # id = params.get("id")

        '''
            to fetch user id( or details) from access token
            use --> request.user.id ( or email, first_name....n)
        '''
        # email = request.user.email
        # print(email)
        #response = super(ProfileAPI, self).post(request, *args, **kwargs)
        #token = Token.objects.get(key=response.data['token'])