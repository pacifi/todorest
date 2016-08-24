"""
Modulo de Urls

Carga las urls del api
"""

from django.conf.urls import url
from .views import HolaMundo, ToDoView, UsuarioApi

urlpatterns = [
    url(r'^hola_mundo_rest/(?P<nombre>\w+)/$', HolaMundo.as_view(), name='hola_mundo'),
    url(r'^usuarios/$', UsuarioApi.as_view(), name='usuarios'),
    url(r'^usuarios/(?P<id>\d+)/$', UsuarioApi.as_view(), name='usuario'),
    url(r'^todos/$', ToDoView.as_view()),
]
