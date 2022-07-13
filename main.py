from models import db, User, Book, BookAuthor, Library, Author, Address, AskBook, Order


def create_tables():
    db.create_tables(
        [User, Book, Library, AskBook, Address, Author, BookAuthor, Order]
    )


if __name__ == '__main__':
    create_tables()
