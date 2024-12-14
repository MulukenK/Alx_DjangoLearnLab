from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer
from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    from django.contrib.auth import authenticate

    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)






User = get_user_model()

class FollowUserView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Get the user to be followed
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Ensure the user doesn't follow themselves
        if request.user == user_to_follow:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        # Add to the 'following' list
        request.user.following.add(user_to_follow)
        return Response({'detail': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)


class UnfollowUserView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Get the user to unfollow
        try:
            user_to_unfollow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Ensure the user is already following the user to unfollow
        if user_to_unfollow not in request.user.following.all():
            return Response({'detail': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)

        # Remove from the 'following' list
        request.user.following.remove(user_to_unfollow)
        return Response({'detail': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
