# Retrieve Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book  # This should output: <Book: 1984>
