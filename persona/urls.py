"""empleado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

# Used to create a namespace for the URL names.
app_name = 'persona_app' 

# A list of URL patterns. 
urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar-todo-empleados/', login_required(views.ListaallEmpleados.as_view()), name='empleados_all'),
    path('listar-by-area/<short_name>/', login_required(views.ListByareaEmpleado.as_view()), name='empleados_area'),
    path('ver-empleado/<pk>/', login_required(views.EmpleadoDetailView.as_view()), name='empleado_detail'),
    path('add-empleado/', login_required(views.EmpleadoCreateView.as_view()), name='empleado_add'),
    path('update-empleado/<pk>/', login_required(views.EmpleadoUpdateView.as_view()), name='modificar_empleado'),
    path('delete-empleado/<pk>/', login_required(views.EmpleadoDeleteView.as_view()), name='eliminar_empleado'),
    path('lista-empleados-admin/', login_required(views.ListaEmpleadosAdmin.as_view()), name='empleados_admin'),
] 