"""
Biblioteca Models
"""

from django.db.models import (
    Model, CharField, EmailField, DateField, ForeignKey, ManyToManyField, PROTECT
)


class Author(Model):
    """
    Author Class
    """
    name = CharField(max_length=120)
    lastname = CharField(max_length=120)
    email = EmailField(max_length=100)

    def __str__(self):
        return f'{self.lastname}, {self.name}'


class Publisher(Model):
    """
    Publisher Class
    """
    name = CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Book(Model):
    """
    Book Class
    """
    title = CharField(max_length=255)
    isbn = CharField(max_length=255, unique=True)
    publisher = ForeignKey(
        Publisher,
        on_delete=PROTECT
    )
    authors = ManyToManyField(Author)
    publication_date = DateField()

    def __str__(self):
        return str(self.title)
