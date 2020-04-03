# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import FormView
import JsonResponse
from django.shortcuts import render
import models


# print create_entity_using_keyword_arguments()


class contact(JsonResponse.JSONResponseMixin, FormView):
    def get(self, request, *args, **kwargs):
        context = models.create_entity_using_keyword_arguments()
        return self.render_to_response(context)

class ssss(JsonResponse.JSONResponseMixin, FormView):
    '''
    A view that renders a template.  This view will also pass into the context
    any keyword arguments passed by the url conf.
    
'''

    def get(self, request, *args, **kwargs):
        context = {"aaaa": "Nguyen Van dadadad "}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = {"aaaa": "Nguyen Van TRung aahahaha  "}
        return self.render_to_response(context)
