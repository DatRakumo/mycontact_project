from google.cloud import ndb


class Account(ndb.Model):
    username = ndb.StringProperty()
    userid = ndb.IntegerProperty()
    email = ndb.StringProperty()


def create_entity_using_keyword_arguments():
    sandy = Account(
        username='Sandy', userid=123, email='sandy@example.com')
    return sandy


client = ndb.Client()
with client.context():
    # Use NDB for some stuff
    print (create_entity_using_keyword_arguments())
    pass
