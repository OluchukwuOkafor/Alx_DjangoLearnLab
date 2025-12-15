from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# -------------------------------
# Author Model
# -------------------------------
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# -------------------------------
# Book Model
# -------------------------------
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Custom validation to prevent future publication year
    def clean(self):
        if self.publication_year > date.today().year:
            raise ValidationError({'publication_year': 'Publication year cannot be in the future.'})
