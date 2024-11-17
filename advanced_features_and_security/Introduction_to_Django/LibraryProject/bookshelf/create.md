
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Comment: Checked success by...
>>> print(book)

OUTPUT:- Book object (1)
