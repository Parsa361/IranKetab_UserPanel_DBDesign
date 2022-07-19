from peewee import Model, CharField, ForeignKeyField, DateField
from playhouse.db_url import connect

# If we use this structure, we can connect to any RDBMS
db = connect('mysql://root:password@127.0.0.1:3306/iranketab')


class BaseModel(Model):
    class Meta:
        database = db

    def __str__(self):
        return str(self.id)


class User(BaseModel):
    username = CharField(max_length=32)
    password = CharField(max_length=32)

    @classmethod
    def authenticate(cls, username,password):
        return cls.select().where(
            cls.username == username, cls.password == password
        ).first()


class Book(BaseModel):
    name = CharField(max_length=32)
    ISBN = CharField(max_length=32)


class Author(BaseModel):
    name = CharField(max_length=32)


class Library(BaseModel):
    name = CharField(max_length=32)
    user = ForeignKeyField(User, backref='libraries')
    book = ForeignKeyField(Book, backref='books')


class AskBook(BaseModel):
    user = ForeignKeyField(User, backref='asks')
    book_name = CharField(max_length=32)
    pub_name = CharField(max_length=32)
    author_name = CharField(max_length=32)
    ISBN = CharField(max_length=32)


class Address(BaseModel):
    user = ForeignKeyField(User, backref='addresses')
    phone = CharField(max_length=32)
    address = CharField(max_length=32)


class Order(BaseModel):
    user = ForeignKeyField(User, backref='orders')
    book = ForeignKeyField(Book, backref='books')
    send_time = DateField(null=True)


class BookAuthor(BaseModel):
    book = ForeignKeyField(Book, backref='authors')
    author = ForeignKeyField(Author, backref='books')
