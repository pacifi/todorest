

from django.conf.urls import url
from .views import HolaMundo

urlpatterns = [
    url(r'^hola_mundo_rest/(?P<nombre>\w+)/$', HolaMundo.as_view())
]
