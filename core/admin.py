from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    '''
        Admin View for ToDo
    '''
    list_display = ('propietario', 'todo', 'hecho',)
    exclude = ['propietario',]
    def save_model(self, request, obj, forms, change):
        obj.propietario = request.user
        obj.save()


admin.site.register(ToDo, ToDoAdmin)