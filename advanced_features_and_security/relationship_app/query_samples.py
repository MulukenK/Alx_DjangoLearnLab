from relationship_app.models import Author, Book, Library, Librarian


author1 = Author.objects.get(name=author_name)
books_by_author = objects.filter(author=author) 
print("Books by J.K. Rowling:")
for book in books_by_author:
    print(book.title)


library = Library.objects.get(name=library_name)
books_in_library = library.books.all() 
print("\nBooks in library_name:")
for book in books_in_library:
    print(book.title)


library = Librarian.objects.get(library=
librarian_for_library = library.librarian  
print(f"\nLibrarian for Central Library: {librarian_for_library.name}")
