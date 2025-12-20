"""
Unit tests for Book API views.
Tests CRUD operations, permissions, filtering, searching, and ordering.
"""

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from api.models import Book, Author


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    """

    def setUp(self):
        """
        Set up test data and user.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create Author instances
        self.author1 = Author.objects.create(name="William")
        self.author2 = Author.objects.create(name="John")

        # Create Book instances
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author=self.author1,
            publication_year=2020
        )

        self.book2 = Book.objects.create(
            title="Advanced Django",
            author=self.author2,
            publication_year=2022
        )

        # API URLs
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book1.id}/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book1.id}/"
        self.delete_url = f"/api/books/delete/{self.book1.id}/"

    # ----------------------------
    # READ TESTS
    # ----------------------------
    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ----------------------------
    # CREATE TESTS
    # ----------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2023
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": self.author1.id,
            "publication_year": 2024
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------------
    # UPDATE TESTS
    # ----------------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Updated Title",
            "author": self.author1.id,
            "publication_year": 2021
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book_unauthenticated(self):
        data = {
            "title": "Hacked Title",
            "author": self.author1.id,
            "publication_year": 2019
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------------
    # DELETE TESTS
    # ----------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------------
    # FILTER / SEARCH / ORDER TESTS
    # ----------------------------
    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url + "?publication_year=2022")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + "?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Django" in book["title"] for book in response.data))

    def test_order_books_by_title(self):
        response = self.client.get(self.list_url + "?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
