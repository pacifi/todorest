"""
Modulo de Urls

Carga las urls del api
"""

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


from .views import HolaMundo, ToDoView, UsuarioApi, UserViewSet, ToDoViewSet

router = DefaultRouter()
router.register(r'miembros', UserViewSet)  # le cambiamos a miembros para ver que todas la urls funcionan
router.register(r'hechos', ToDoViewSet)

urlpatterns = [
    url(r'^hola_mundo_rest/(?P<nombre>\w+)/$', HolaMundo.as_view(), name='hola_mundo'),
    url(r'^usuarios/$', UsuarioApi.as_view(), name='usuarios'),
    url(r'^usuarios/(?P<id>\d+)/$', UsuarioApi.as_view(), name='usuario'),
    url(r'^users/$', UsuarioApi.as_view(), name='usuarios'),  # con model view
    url(r'^user/(?P<id>\d+)/$', UsuarioApi.as_view(), name='usuario'),  # model view
    url(r'^todos/$', ToDoView.as_view()),

    url(r'^', include(router.urls)),

]
