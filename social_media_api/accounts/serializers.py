from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

# Get the custom user model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Fields for password and password confirmation
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
        """Validate that the two passwords match."""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        """Create a new user instance."""
        validated_data.pop('password2', None)  # Remove password2 from the data
        password = validated_data.pop('password')  # Extract password

        # Create user using Django's user creation method
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)  # Set the password
        user.save()

        # Create an auth token for the user
        Token.objects.create(user=user)

        return user