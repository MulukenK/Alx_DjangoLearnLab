from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Post
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

# Post ViewSet with permissions to ensure users can only modify their own posts
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Return posts created by the logged-in user or all posts if the user is an admin
        if self.request.user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)

# Comment ViewSet with permissions to ensure users can only modify their own comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Return comments for the post created by the logged-in user
        return Comment.objects.filter(author=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']


class PostFeedPagination(PageNumberPagination):
    page_size = 10  # Adjust the page size as needed

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = PostFeedPagination

    def get_queryset(self):
        # Return posts from the users the current user is following
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
    



User = get_user_model()

class FeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get the current authenticated user
        user = self.request.user

        # Get all users that the current user follows
        following_users = user.following.all()

        # Return posts from followed users, ordered by creation date
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    



@api_view(['POST'])
def like_post(request, pk):
    # Use generics.get_object_or_404 to retrieve the post
    post = get_object_or_404(Post, pk=pk)

    # Ensure the user has not already liked the post
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create a notification for the post author
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked your post",
        target=post
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unlike_post(request, pk):
    # Use generics.get_object_or_404 to retrieve the post
    post = get_object_or_404(Post, pk=pk)

    # Find the like object and delete it
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Like.DoesNotExist:
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)