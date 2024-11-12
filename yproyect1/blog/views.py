from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
# mi_app/views.py
from django.shortcuts import render
from .forms import ContactForm

def formulario_vista(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            # Aquí puedes manejar los datos (guardarlos, enviarlos por email, etc.)
    
    return render(request, 'mi_app/formulario.html', {'form': form})
