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
		return obj[0]   # id = 0,1,2,3,4,5,....

	def get1_book(cls):
		obj = cls.query(cls.author == "Nguyen Van Dat").fetch()
		return obj[1]   # id = 0,1,2,3,4,5,....

	@classmethod
	def get_book(cls):
		query = Greeting.query(Greeting.allocate_ids == 4785074604081152).fetch()
		return query









