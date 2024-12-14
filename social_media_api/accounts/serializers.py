from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# Get the custom user model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Use CharField for password and confirm password fields
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        help_text="Enter a strong password"
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        label="Confirm Password",
        help_text="Re-enter the password for confirmation"
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2', 'bio', 'profile_picture']

    def validate(self, attrs):
        """Ensure the passwords match"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        """Create the user and return the user instance"""
        validated_data.pop('password2', None)  # Remove password2, it's not part of the user model
        password = validated_data.pop('password')  # Extract password

        # Create a user using the custom user model's create_user method
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)  # Set the password
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user