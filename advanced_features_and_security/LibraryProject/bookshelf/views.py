from django.shortcuts import render

# Create your views here.
# views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MetaModel
from .models import Book
from .forms import ExampleForm

def book_search(request):
    form = ExampleForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['q']
        books = Book.objects.filter(title__icontains=query)
        return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
    return render(request, 'bookshelf/book_list.html', {'form': form})

@permission_required('yourapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'yourapp/book_list.html', {'books': books})

@permission_required('yourapp.can_create', raise_exception=True)
def books(request):
    if request.method == "POST":
        # Code to add a new book entry
        return redirect('book_list')
    return render(request, 'yourapp/books.html')