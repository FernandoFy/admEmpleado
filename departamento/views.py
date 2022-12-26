from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from persona.models import Empleado
from django.views.generic import ListView
from .models import Departamento
from django.urls import reverse_lazy

# Create your views here.

# This class is a subclass of ListView, and it will display a list of Departamento objects in the
# template list_depto.html, and the list of objects will be called departamentos in the template.
class DepartamentoListView(ListView):
    template_name = "departamento/list_depto.html"
    model = Departamento
    context_object_name = "departamentos"


# It creates a new department.
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamento_app:departamento_list')

    def form_valid(self, form):
        """
        It saves the form data to the database and then returns the form data to the template
        
        :param form: The form that was submitted
        :return: The super class form_valid method is being returned.
        """
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname']
        )
        depa.save()
        return super(NewDepartamentoView, self).form_valid(form)


        