from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register_view,
    CustomLoginView,
    CustomLogoutView,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # Existing routes
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Role-based access views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Custom permission-protected book views
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]
