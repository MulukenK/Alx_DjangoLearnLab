from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import add_comment, edit_comment, delete_comment
from .views import search_posts, posts_by_tag

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/edit/', edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete-comment'),
    path('comment/<int:pk>/update/', views.edit_comment, name='edit_comment')
    path('post/<int:pk>/comments/new/', views.delete_comment, name='delete-comment')
    path('search/', search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),
    path('tags/<slug:tag_slug>/", "PostByTagListView.as_view()'),
]


