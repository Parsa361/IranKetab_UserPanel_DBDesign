from models import User, BookAuthor, Book, Author


def show_users():
    users = User.select()
    for user in users:
        print(user.username)


def show_user_data(username="Majid", password="Majed@021"):
    user = User.authenticate(username, password)
    if user is None:
        return
    library = user.libraries.get()
    print(f"User:{user.username}\n\tLibrary Name:{library.name}\t\tBook Name:{library.book.name}"
          f"\t\tBook ISBN:{library.book.ISBN}\n", "# " * 80)


def show_books():
    books = Book.select()
    for book in books:
        authors = ', '.join([book_author.author.name for book_author in book.authors])
        print(f"{book.name}({book.ISBN})", "\t", authors)
