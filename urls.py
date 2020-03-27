from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from ApiContact.views import ssss,Contact

urlpatterns = [
    url(r'^', TemplateView.as_view(template_name='index.html')),
    url(r'hello', RedirectView(template_name='home.html')),
    url(r'good', ssss.as_view(), name='show'),
    url(r'contact', Contact.as_view(), name='contact'),

]