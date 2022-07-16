import json
from models import User, Book, Author, BookAuthor, Library


class BaseImporter:
    filename = None
    model = None

    @classmethod
    def load(cls):
        with open(f"fixtures/{cls.filename}.json") as f:
            data = json.loads(f.read())

            instances = []
            for instance in data:
                instances.append(cls.model.create(**instance))

            return instances


class UserImporter(BaseImporter):
    filename = 'users'
    model = User


class BookImporter(BaseImporter):
    filename = 'books'
    model = Book


class AuthorImporter(BaseImporter):
    filename = 'authors'
    model = Author


class LibraryImporter(BaseImporter):
    filename = 'libraries'
    model = Library


class BookAuthorImporter(BaseImporter):
    filename = 'books-authors'
    model = BookAuthor

