import json

from api import JsonResponse
from models._greeting import Greeting
from django.views.generic import FormView


class Greetings(JsonResponse.JSONResponseMixin, FormView):

    def post(self, request, *args, **kwargs):
        body_unicode = self.request.body
        body = json.loads(body_unicode)

        greeting_name = body['greeting_name']
        content = body['content']
        author = body['author']

        g = Greeting.insert(greeting_name, content, author)

        context = {
            'id': g.key.id(),
            'author': g.author,
            'content': g.content,
            'greeting_name': g.greeting_name,
            'avatar': g.avatar,
            'created_date': g.created_date.isoformat(),
            'updated_date': g.updated_date.isoformat()
        }

        return self.render_to_response(context)


    def get(self, request, *args, **kwargs):
        greet = Greeting.query_book()
        context = {
            'id': greet.key.id(),
            'author': greet.author,
            'content': greet.content,
            'greeting_name': greet.greeting_name,
        }
        return self.render_to_response(context)

""" 
    def get(self, request, *args, **kwargs):
        greet = Greeting.get_book()
        context = {
            'id': greet.key.id(),
            'author': greet.author,
            'content': greet.content,
            'greeting_name': greet.greeting_name,
        }
        return self.render_to_response(context)


    def get(self, request, *args, **kwargs):
        greet = Greeting.get_book(1)
        context = {
            'id': greet.key.id(),
            'author': greet.author,
            'content': greet.content,
            'greeting_name': greet.greeting_name,
            'avatar': greet.avatar,
            'created_date': greet.created_date.isoformat(),
            'updated_date': greet.updated_date.isoformat()

        }
        return self.render_to_response(context)
    """



