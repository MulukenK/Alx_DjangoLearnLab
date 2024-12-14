from django.urls import path
from accounts import views
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]


