from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from api.api_view import Greetings

urlpatterns = [
    url(r'^api/insert', Greetings.as_view()),
    url(r'^api/get/(?P<id>[0-9]+)/$',Greetings.as_view()),
    url(r'hello', RedirectView(template_name='home.html')),

]