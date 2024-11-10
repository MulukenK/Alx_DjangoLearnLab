from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (e.g., "J.K. Rowling")
author = Author.objects.get(name="J.K. Rowling")
books_by_author = author.books.all()  # Accessing related books via related_name
print("Books by J.K. Rowling:")
for book in books_by_author:
    print(book.title)

# List all books in a library (e.g., "Central Library")
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()  # Accessing related books in the library
print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a specific library (e.g., "Central Library")
library = Library.objects.get(name="Central Library")
librarian_for_library = library.librarian  # Access the related librarian
print(f"\nLibrarian for Central Library: {librarian_for_library.name}")
