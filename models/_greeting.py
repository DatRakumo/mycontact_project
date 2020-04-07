from google.appengine.ext import ndb
#from google.cloud import ndb

class Greeting(ndb.Model):
	content = ndb.StringProperty()
	author = ndb.StringProperty()
	greeting_name = ndb.StringProperty()
	updated_by = ndb.StringProperty()
	avatar = ndb.StringProperty(default='')
	created_date = ndb.DateTimeProperty(auto_now_add=True)
	updated_date = ndb.DateTimeProperty(auto_now=True)


	@classmethod
	def insert(cls, greeting_name, content, author):
		g = Greeting()
		g.content = content
		g.greeting_name = greeting_name
		g.author = author
		g.put()
		return g

	@classmethod
	def query_book(cls):
		obj = cls.query().fetch()
		return obj[1]    # id = 0,1,2,3,4,5,....

	@classmethod
	def update_entity(cls):
		obj = cls.query().fetch()
		obj[1].author = "aaaaaaaaaaa"
		return obj[1]










