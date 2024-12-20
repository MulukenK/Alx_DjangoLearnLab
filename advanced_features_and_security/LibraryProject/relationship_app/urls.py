
from django.urls import path
from .views import list_books
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'), 
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name=", "LoginView.as_view(template_name=, name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('book/add/', views.add_book, name='add_book/'),
    path('book/edit/<int:pk>/', views.edit_book, name='edit_book/'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book/'),
    
]


