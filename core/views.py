from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from core.models import Contato


# Create your views here.
# lista todos os contatos
def contatos(request):
    contacts = Contato.objects.all()
    dados = {'contacts': contacts}
    return render(request, 'lista.html', dados)

class ContatoCreateView(CreateView):
    model = Contato
    fields = ('nome', 'whatsapp', 'twitter', 'facebook', 'instagram', 'linkedin')

# janela de cadastro de novo contato
def contato(request):
    return render(request, 'contato2.html')