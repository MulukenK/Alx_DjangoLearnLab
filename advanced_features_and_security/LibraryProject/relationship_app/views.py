from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from django.shortcuts import render
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # Assuming you have a BookForm for adding/editing books

# View for adding a book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list or a confirmation page
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# View for editing a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

# View for deleting a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list
    return render(request, 'delete_book.html', {'book': book})


# Helper function to check if the user has the required role
def role_required(role):
    def decorator(view_func):
        return user_passes_test(
            lambda user: user.userprofile.role == role, 
            login_url='login'
        )(view_func)
    return decorator

# Admin view
@user_passes_test('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view (Django's built-in view)
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Logout view (Django's built-in view)
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
