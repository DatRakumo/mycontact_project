from django.conf.urls import url
from django.views.generic import TemplateView
from views import ssss,contact
from polls.views import HomePageView,geeks_view
from bookstore import views




urlpatterns = [
    url(r'home', TemplateView.as_view(template_name='index.html')),
    url(r'hello', TemplateView.as_view(template_name='home.html')),
    url(r'good', ssss.as_view(), name='show'),
    url(r'hi', HomePageView.as_view(), name='hi'),
    url(r'map', geeks_view, name='map'),
    url(r'contact', contact.as_view(), name='contact'),
    url(r'bookstore', views.home, name='home'),
]

