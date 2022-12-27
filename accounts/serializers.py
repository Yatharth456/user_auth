from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Address, CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

# User Serializer
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = IsAuthenticated(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            #update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
            }

            return validation
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email', 'password', 'first_name', 'last_name', 'role', 'hourly_rate')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        # user.role = role
        # user.save()
        return user
        print(user)

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'role'
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('users','first_name', 'last_name', 'gender', 'mobile_no', 'image', 'zip_code')
        extra_kwargs = {'users': {'required': True}}

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'users', 'address','mobile_no2')


class UpdateHourlyRate(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('hourly_rate',)