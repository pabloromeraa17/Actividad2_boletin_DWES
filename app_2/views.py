from django.shortcuts import render
from .forms import Formulario
# Create your views here.
def index(request):
    valido = None
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            valido = "Valido el FORMULARIO"
    else:
        form = Formulario()
    return render(request, 'index.html', {
        'form': form, 'valido': valido
    })