from importer import UserImporter, BookImporter, AuthorImporter, LibraryImporter, BookAuthorImporter

from models import db, User, Book, BookAuthor, Library, Author, Address, AskBook, Order

from reports import show_users, show_books


def create_tables():
    db.create_tables(
        [User, Library, AskBook, Address, Author, BookAuthor, Order, Book]
    )


def load_data():
    importer_classes = [
        UserImporter, BookImporter, AuthorImporter,
        LibraryImporter, BookAuthorImporter
    ]
    for _class in importer_classes:
        print(_class.load())


def show_data():
    print("#" * 50)
    show_users()
    print("#" * 50)
    show_books()


if __name__ == '__main__':
    # create_tables()
    # load_data()
    show_data()
