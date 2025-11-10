from django.urls import path
from .views import list_books, LibraryDetailView, register_view, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view
    path('register/', register_view, name='register'),  # user registration
    path('login/', CustomLoginView.as_view(), name='login'),  # login
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # logout
]
