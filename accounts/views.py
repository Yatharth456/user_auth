from django.shortcuts import render
# Create your views here.
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserListSerializer, RegisterSerializer, ProfileSerializer, AddressSerializer
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.decorators import IsAdmin, IsEmployee, IsManager
from rest_framework.response import Response
from rest_framework import permissions
import jwt
from datetime import timezone, datetime, timedelta
from accounts.decorators import CustomerAccessPermission, AdminPermission, ManagerPermission, EmployeePermission
#from accounts.serializers import MyTokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#from .models import CustomUser
from django.conf import settings
from accounts.models import Profile, Address

class LoginAPI(APIView):
    #serializer_class = MyTokenObtainPairSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        
        data = {
            'id': user.id,
            'role': user.role,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        # SECRET_KEY = settings.SECRET_KEY
        # encoded_jwt = jwt.encode({"exp": datetime.now(tz=timezone.utc) + timedelta(days=1),"data": data}, "secret", algorithm="HS256")

        return Response(
            {
                #  "access": encoded_jwt,
                **data

            }
            , status=200
        )
        #return Response(data, status=200)
            
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
    permission_classes = [permissions.IsAuthenticated,]

    # class CustomerAccessPermission(permissions.BasePermission):
    #     def has_permission(self, request, view):
    #         if request.method == 'POST':
    #             return True
    #         return False
            
    def post(self, request, *args, **kwargs):
        data = request.data
        data["users"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"profile": serializer.data})



class AllProfileAPI(generics.GenericAPIView):
    serializer_class= ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, AdminPermission]

    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        serializer = self.serializer_class(profiles, many=True)
        return Response({"profiles": serializer.data})

class managerAPI(generics.GenericAPIView):
    serializer_class= AddressSerializer
    permission_classes = [permissions.IsAuthenticated,]
 
    def get(self, request, *args, **kwargs):
        addresses = Address.objects.all()
        serializer = self.serializer_class(addresses, many=True)
        return Response({"addresses": serializer.data})