
from google.cloud import ndb


# [END ndb_import]
class Book(ndb.Model):
    title = ndb.StringProperty()


# [START ndb_client]
client = ndb.Client()


# [END ndb_client]
def list_books():
    with client.context():
        books = Book.query()
        for book in books:
            print(book.to_dict())
# [END ndb_context_usage]


if __name__ == "__main__":
    Book.list_books()