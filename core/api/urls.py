"""
Modulo de Urls

Carga las urls del api
"""

from django.conf.urls import url
from .views import HolaMundo, UsuarioApi

urlpatterns = [
    url(r'^hola_mundo_rest/(?P<nombre>\w+)/$', HolaMundo.as_view()),
    url(r'^usuarios/$', UsuarioApi.as_view()),
    url(r'^usuarios/(?P<id>\d+)/$', UsuarioApi.as_view()),
]
