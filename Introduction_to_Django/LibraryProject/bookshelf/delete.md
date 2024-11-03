>>> book.delete()
(1, {'bookshelf.Book': 1})

Comment: Checked success by....
>>> books = Book.objects.all()
>>> print(list(books))

OUTPUT:- []