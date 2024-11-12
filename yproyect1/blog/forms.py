# mi_app/forms.py
from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo electrónico')
