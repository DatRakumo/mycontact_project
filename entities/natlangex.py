from google.cloud import ndb


class Book(ndb.Model): # create object Book ===> table : Book have field : title (string)
    title = ndb.StringProperty()  # property "title " with style "string"


client = ndb.Client()


def list_books():
    with client.context():
        books = Book.query()
        for book in books:
            print(book.to_dict())