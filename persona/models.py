from django.db import models
from departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

# It creates a table in the database called Habilidades with a column called habilidad.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

# It creates a table in the database with the name Habilidades.
    class Meta:
        verbose_name_plural = 'Habilidades'
        verbose_name = 'Habilidad Empleados'

    def __str__(self):
        """
        The function __str__() is a special function in Python classes. It is used to control how variables
        are displayed when using functions like print()
        :return: The id and the habilidad
        """
        return str(self.id) + '-' + self.habilidad

# It creates a class called Empleado that inherits from the Model class.
class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'contador'),
        ('1', 'administrador'),
        ('2', 'informatico'),
        ('3', 'marketing'),
        ('4', 'servicio al cliente'),
    ) 

# Creating a table in the database called Empleado with the columns first_name, last_name, full_name,
# job, departamento, avatar, habilidades, and hoja_vida.
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

# A model for the database.
    class Meta:
        verbose_name_plural = 'Empleados'
        verbose_name = 'EMPLEADOS'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')
 
    def __str__(self):
        """
        The __str__ function is a special function in Python classes. It is used to control how an object is
        printed out when you use the print function
        :return: The id, first name, last name, and job of the employee.
        """
        return str(self.id) + '-' + self.first_name + '-' + self.last_name + '-' + self.job