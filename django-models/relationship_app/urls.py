
from django.urls import path
from .views import list_books
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'), 
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name=", "LoginView.as_view(template_name=, name='logout'),
    path('register/', views.register, name='register'),
    
]
