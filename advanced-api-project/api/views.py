# api/views.py

"""
This module contains all API views for the Book model.
It uses Django REST Framework generic views to handle CRUD operations
and supports filtering, searching, and ordering.
"""

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer


# ----------------------------
# LIST VIEW (Filtering, Search, Ordering)
# ----------------------------
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Allows filtering, searching, and ordering.
    Read-only access is allowed for unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # Fields available for filtering
    filterset_fields = ['title', 'publication_year', 'author']

    # Fields available for search
    search_fields = ['title', 'author__name']

    # Fields available for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


# ----------------------------
# DETAIL VIEW
# ----------------------------
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
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ----------------------------
# UPDATE VIEW
# ----------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ----------------------------
# DELETE VIEW
# ----------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
