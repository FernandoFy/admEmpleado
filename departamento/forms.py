from django import forms


# It creates a form with two fields, departamento and shortname.
class NewDepartamentoForm(forms.Form):
    departamento = forms.CharField(max_length=50)
    shortname = forms.CharField(max_length=50)

    