from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# Get the custom user model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2', 'bio', 'profile_picture']
    
    def validate(self, attrs):
        # Ensure password and password2 match
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs
    
    def create(self, validated_data):
        # Remove password2 as it's not part of the user model
        validated_data.pop('password2', None)
        password = validated_data.pop('password')
        
        # Create the user
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        
        # Create an auth token for the new user
        Token.objects.create(user=user)
        
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        
        if not user:
            raise serializers.ValidationError({"detail": "Invalid credentials."})
        
        attrs['user'] = user
        return attrs