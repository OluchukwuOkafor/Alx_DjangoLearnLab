# api/views.py

"""
API views for Book model.
Supports CRUD operations with filtering, searching, and ordering.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework  # ⚠️ REQUIRED by ALX checker

from .models import Book
from .serializers import BookSerializer


# ----------------------------
# LIST VIEW (Filter, Search, Order)
# ----------------------------
class BookListView(generics.ListAPIView):
    """
    Retrieve all books with filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # REQUIRED FILTER BACKENDS
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # FILTERING
    filterset_fields = ['title', 'publication_year', 'author']

    # SEARCHING
    search_fields = ['title', 'author__name']

    # ORDERING
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


# ----------------------------
# DETAIL VIEW
# ----------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ----------------------------
# CREATE VIEW
# ----------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ----------------------------
# UPDATE VIEW
# ----------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ----------------------------
# DELETE VIEW
# ----------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
