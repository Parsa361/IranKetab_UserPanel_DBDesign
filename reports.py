from models import User, BookAuthor, Book


def show_users():
    users = User.select()
    for user in users:
        print(user.username)


def show_books():
    books = Book.select()
    for book in books:
        authors = ', '.join([book_author.author.name for book_author in book.authors])
        print(f"{book.name}({book.ISBN})", "\t", authors)

