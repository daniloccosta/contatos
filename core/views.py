from django.shortcuts import render, HttpResponse, redirect
from core.models import Contato
from django.http.response import Http404
# Create your views here.

# lista todos os contatos
def contatos(request):
    contacts = Contato.objects.all()
    dados = {'contacts': contacts}
    return render(request, 'lista.html', dados)

# janela de cadastro de novo contato
def contato(request):
    dados = {}
    id = request.GET.get('id')
    if id:
        dados['contato'] = Contato.objects.get(id=id)
    return render(request, 'contato.html', dados)

def gravar_contato(request):
    if request.POST:
        id_contato = request.POST.get('id')
        nome = request.POST.get('nome')
        facebook = request.POST.get('facebook')
        whatsapp = request.POST.get('whatsapp')
        instagram = request.POST.get('linkedin')
        twitter = request.POST.get('twitter')
        linkedin = request.POST.get('linkedin')
        tiktok = request.POST.get('tiktok')
        if id_contato:
            contato = Contato.objects.get(id=id_contato)
            contato.nome = nome
            contato.facebook = facebook
            contato.whatsapp = whatsapp
            contato.instagram = instagram
            contato.twitter = twitter
            contato.linkedin = linkedin
            contato.tiktok = tiktok
            contato.save()
        else:
            Contato.objects.create(nome=nome, facebook=facebook, whatsapp=whatsapp, instagram=instagram,
                                twitter=twitter, linkedin=linkedin, tiktok=tiktok)
    return redirect('/')

def delete_contato(request):
    try:
        id = request.GET.get('id')
    except:
        raise Http404()

    contato = Contato.objects.get(id=id)
    contato.delete()
    return redirect('/')