from importer import UserImporter, BookImporter, AuthorImporter, LibraryImporter, BookAuthorImporter

from models import db, User, Book, BookAuthor, Library, Author, Address, AskBook, Order

from reports import show_users


def create_tables():
    db.create_tables(
        [User, Book, Library, AskBook, Address, Author, BookAuthor, Order]
    )


def load_data():
    importer_classes = [
        UserImporter, BookImporter, AuthorImporter,
        LibraryImporter, BookAuthorImporter
    ]
    for _class in importer_classes:
        print(_class.load())


if __name__ == '__main__':
    # create_tables()
    load_data()

