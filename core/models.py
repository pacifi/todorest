from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_finalizado = models.DateTimeField()
    propietario = models.ForeignKey(User)
    todo = models.TextField()
    hecho = models.BooleanField(default=False)

    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDos"

    def __str__(self):
        return u"{0} - {1}".format(self.todo, self.propietario.username)
    