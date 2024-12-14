from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Post

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