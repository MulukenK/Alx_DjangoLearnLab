
>>> book = Book.objects.get(title="1984")

comment: Checked success by...
>>> print(book.title, book.author, book.publication_year)

OUTPUT:- 1984 George Orwell 1949