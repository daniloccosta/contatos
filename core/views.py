from django.shortcuts import render, HttpResponse, redirect
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
    fields = ('nome', 'whatsapp', 'twitter', 'facebook', 'instagram', 'linkedin', 'tiktok')

# janela de cadastro de novo contato
def contato(request):
    return render(request, 'contato2.html')

def gravar_contato(request):
    if request.POST:
        id_contato = request.POST.get('id_contato')
        nome = request.POST.get('nome')
        whatsapp = request.POST.get('whatsapp')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('linkedin')
        if id_contato:
            contato = Contato.objects.get(id=id_contato)
            contato.nome = nome
            contato.whatsapp = whatsapp
            contato.twitter = twitter
            contato.facebook = facebook
            contato.instagram = instagram
            contato.save()
        else:
            Contato.objects.create(nome=nome, whatsapp=whatsapp, twitter=twitter, facebook=facebook,
                                   instagram=instagram)
    return redirect('/')