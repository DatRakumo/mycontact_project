from google.cloud import ndb

class Book (ndb.model):
    title = ndb.StringProperty()
    author = ndb.StringProperty()
    coppyright_year = ndb.IntegerProperty()
    author_birthday = ndb.DateProperty()

class BookReview (ndb.model):
    book = ndb.KeyProperty(kind='book')
    title = ndb.StringProperty()
    author = ndb.StringProperty()
    coppyright_year = ndb.IntegerProperty()
    author_birthday = ndb.DateProperty()
    review_author = ndb.UserProperty()
    review_text =ndb.TextProperty()




