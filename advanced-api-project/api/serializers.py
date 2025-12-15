from rest_framework import serializers
from datetime import date
from .models import Author, Book

# -----------------------------------
# Book Serializer
# -----------------------------------
class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model data.
    Includes validation to ensure publication year is not in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Ensure publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value
# -----------------------------------
# Author Serializer
# -----------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model.
    Includes a nested list of related books.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
