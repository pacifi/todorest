"""Modulo Todo Model."""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ToDo(models.Model):
    """Django Model."""

    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_finalizado = models.DateTimeField()
    propietario = models.ForeignKey(User)
    todo = models.TextField()
    hecho = models.BooleanField(default=False)

    class Meta:
        """Model Meta."""

        verbose_name = "ToDo"
        verbose_name_plural = "ToDos"

    def __str__(self):
        """Str Todo."""
        return u"{0} - {1}".format(self.todo, self.propietario.username)
