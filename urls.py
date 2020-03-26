from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    url(r'^', TemplateView.as_view(template_name='index.html')),
    url(r'hello', RedirectView(template_name='home.html')),
]