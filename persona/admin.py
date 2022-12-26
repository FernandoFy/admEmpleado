from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class Empleadoadmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job', 
        'nombre_completo',
    )

    def nombre_completo(self, obj):
        print(obj)
        return obj.first_name + ' ' + obj.last_name

    #añade un buscador que busca mediante el atributo dado
    search_fields = ('first_name',)
    #añade un filtro del atributo dado
    list_filter = ('departamento', 'job', 'habilidades')
    #Este parametro solo funciona con las relaciones o campos m:n [Esto añade un filtro para buscar y escoger las habilidades]
    filter_horizontal = ('habilidades',)

# Registering the Empleado model with the Empleadoadmin class.
admin.site.register(Empleado, Empleadoadmin)