from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book
from django.urls import reverse


class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(
            title="Book 1",
            publication_year=2024,
            author=self.author
        )
        self.book_list_url = reverse('book-list')  # Ensure you name the URL path
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.id})

def test_create_book(self):
    data = {
        "title": "Book 2",
        "publication_year": 2023,
        "author": self.author.id
    }
    response = self.client.post(self.book_list_url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 2)
    self.assertEqual(Book.objects.last().title, "Book 2")

def test_retrieve_book(self):
    response = self.client.get(self.book_detail_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], self.book.title)

def test_update_book(self):
    data = {"title": "Updated Book"}
    response = self.client.patch(self.book_detail_url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book.refresh_from_db()
    self.assertEqual(self.book.title, "Updated Book")

def test_delete_book(self):
    response = self.client.delete(self.book_detail_url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 0)

def test_filter_books_by_author(self):
    response = self.client.get(self.book_list_url, {'author': self.author.id})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

def test_search_books_by_title(self):
    response = self.client.get(self.book_list_url, {'search': 'Book 1'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)

def test_order_books_by_publication_year(self):
    response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertGreaterEqual(
        response.data[0]['publication_year'], response.data[-1]['publication_year']
    )

def test_permissions(self):
    response = self.client.post(self.book_list_url, {})
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

def test_create_book_authenticated(self):
        # Explicitly use self.client.login as required
        login_successful = self.client.login(username='testuser', password='testpass')
        self.assertTrue(login_successful, "Login failed with valid credentials.")

         # Test creating a book
        response = self.client.post('/books/', {
            "title": "Test Book",
            "publication_year": 2023,
            "author": 1,  # Replace with an existing author ID
        })
        self.assertEqual(response.status_code, 201)