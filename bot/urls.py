from django.conf.urls import url
from . import views

from .views import QuotesBotView



urlpatterns = [

    url(r'^(?P<accord>\w+)/$', views.index, name='index'),
    url(r'^incoming-message/?$', QuotesBotView.as_view()) 

]