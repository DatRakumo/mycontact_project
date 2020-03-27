# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.views.generic import FormView
from django.http import HttpResponse
from django.views.generic import FormView
import JsonResponse
from django.shortcuts import render_to_response
from models import Account

""" 
class Contact(self,request):
    def foo(request, ):
        return render_to_response("home.html",
                                  {"acounts": Account.objects.create_entity_using_attributes()})

"""

class Contact(JsonResponse.JSONResponseMixin, FormView):
    def get(self, request, *args, **kwargs):
        context = Account.get_by_id()
        return self.render_to_response(context)

class ssss(JsonResponse.JSONResponseMixin, FormView):
    """
    A view that renders a template.  This view will also pass into the context
    any keyword arguments passed by the url conf.
    """

    def get(self, request, *args, **kwargs):
        context = {"aaaa": "Nguyen Van dadadad "}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = {"aaaa": "Nguyen Van dadadad "}
        return self.render_to_response(context)
