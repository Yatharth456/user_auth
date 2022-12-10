from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # create user 
        user = User.objects.create(
            url = validated_data['url'],
            email = validated_data['email'],
            address = validated_data['address'],
            profile = validated_data['profile'],)
        profile_data = validated_data.pop('profile')

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'users','first_name', 'last_name', 'gender', 'mobile_no', 'image', 'zip_code')
        extra_kwargs = {'password': {'write_only': True}}

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'users', 'address','mobile_no2')
        extra_kwargs = {'password': {'write_only': True}}