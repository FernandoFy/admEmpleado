from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)
    anulate = models.BooleanField('Anulate', default=False)

# A model for the database.
    class Meta:
        verbose_name_plural = 'areas de la empresa'
        verbose_name = 'Mi Departamento'
        ordering = ['-name']
        unique_together = ('name', 'short_name')

    def __str__(self):
        """
        The function __str__() is a special function in Python classes. It is used to control how the object
        is printed
        :return: The id, name, and short_name of the object.
        """
        return str(self.id) + '-' + self.name + '-' + self.short_name