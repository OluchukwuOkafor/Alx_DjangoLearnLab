# api/views.py

"""
This module contains all API views for the Book model.
We use Django REST Framework generic views to handle CRUD operations.
"""

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ----------------------------
# LIST VIEW
# ----------------------------
# Allows anyone (authenticated or not) to view all books
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Read-only access is allowed for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------
# DETAIL VIEW
# ----------------------------
# Allows anyone to view a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by its ID.
    Read-only access is allowed for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------
# CREATE VIEW
# ----------------------------
# Only authenticated users can create books
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book instance.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# UPDATE VIEW
# ----------------------------
# Only authenticated users can update books
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# DELETE VIEW
# ----------------------------
# Only authenticated users can delete books
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
