from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import InputForm
from .models import Portadata

# Create your views here.

def index(request):
    datos= Portadata.objects.all()
    #crea diccionario

    context = {
        "datos":datos
    }
    
    return render(request,"portafolio/index.html",context)


@login_required
def form_view(request):
    template = "form.html"
    form= InputForm(request.POST)

    if form.is_valid():
        Portadata.objects.create(**form.cleaned_data)


    contexto = {
        'form': form
        
    }
    return render(request,template,contexto)