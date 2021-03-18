from django.shortcuts import render, HttpResponse, redirect
from core.models import Contato

# Create your views here.
def contatos(request):
    contatos = Contato.objects.all()
    if contatos is not None:
        return render(request, 'contatos.html', contatos)
    else:
        return redirect('/')