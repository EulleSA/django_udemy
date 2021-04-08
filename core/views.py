from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso')
            form = ContatoForm()
        else:
            
            messages.error(request, 'Erro ao enviar e-mail')

    context = {'form':form}
    return render(request, 'core/contato.html', context)

def produto(request):
    return render(request, 'core/produto.html')