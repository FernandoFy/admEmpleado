from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

# InicioView is a class that inherits from TemplateView. 
# 
# The class has a single attribute, template_name, which is set to the string 'inicio.html'
class InicioView(TemplateView):
    template_name = 'inicio.html'


#                   [ListView]

# A class based view that inherits from ListView. It is a generic view that displays a list of
# objects.
class ListaallEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'

    def get_queryset(self):
        """
        The function get_queryset() is called by the ListView class to get the list of objects to display
        :return: A list of objects.
        """
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )      
        print('lista resultado', lista)
        return lista


# A class based view that inherits from ListView. It is a view that displays a list of objects.
class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

    def get_queryset(self):
        """
        The function get_queryset() is called by the ListView class to get the list of objects to display
        :return: A list of objects.
        """
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )      
        print('lista resultado', lista)
        return lista


# This class is a subclass of ListView, and it will render the template 'persona/list_by_area.html'
# and pass the context variable 'empleados' to the template. The queryset will be a list of Empleado
# objects filtered by the short_name of the area.
class ListByareaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista


#           [DetailView]

# The EmpleadoDetailView class inherits from the DetailView class, and it overrides the
# get_context_data() method
class EmpleadoDetailView(DetailView):
    model = Empleado 
    template_name = 'persona/detail_empleado.html'

    def get_context_data(self, **kwargs):
        """
        It takes the context dictionary that the parent class (DetailView) has already created, adds a new
        key-value pair to it, and then returns the updated context dictionary
        :return: The context is being returned.
        """
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = '"Empleado del mes"'
        return context


#                   [CreateView]

# "When the form is valid, save the form, but don't commit it to the database yet. 
# Then, set the fullname field to the first_name and last_name fields, and then save the form to the
# database."
class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_all')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.fullname = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form) 


#                   [UpdateView]

# The EmpleadoUpdateView class inherits from UpdateView, which is a generic view that displays a form
# for editing an existing object, and saves changes to that object
class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
            'first_name', 
            'last_name',
            'job',
            'departamento', 
            'habilidades', ]
    success_url = reverse_lazy('persona_app:empleados_admin')
 
    def post(self, request, *args, **kwargs):
        """
        The function is called when the form is submitted. It gets the object that the form is editing,
        prints the POST data, and then calls the superclass's post function
        
        :param request: The request object
        :return: The form is being returned.
        """
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the form and redirect to the success url
        
        :param form: The form that was submitted
        :return: The super class method form_valid is being returned.
        """
        return super(EmpleadoUpdateView, self).form_valid(form)


#                   [DeleteView]

# This class is a view that displays a confirmation page and deletes an object based on the POST
# method.
class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin') 

    


