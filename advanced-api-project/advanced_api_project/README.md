# Advanced API Project

## Book API Views

This project uses Django REST Framework generic views to handle CRUD operations
for the Book model.

### Available Endpoints

- GET /api/books/ → List all books
- GET /api/books/<id>/ → Retrieve a single book
- POST /api/books/create/ → Create a new book (authenticated users only)
- PUT /api/books/<id>/update/ → Update a book (authenticated users only)
- DELETE /api/books/<id>/delete/ → Delete a book (authenticated users only)

### Permissions

- Read operations are open to all users.
- Write operations require authentication.
