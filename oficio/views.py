import os
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.template.loader import get_template
from xhtml2pdf import pisa

from oficio.forms import FormOficio
from oficio.mascaras import cnpj
from oficio.models import Oficio, Responsavel, Cargo


@login_required
def oficio(request):
    lista_oficios = Oficio.objects.filter(responsavel__usuario=request.user).order_by('numero')
    context = RequestContext(request)
    return render(request, 'oficio.html', {'lista_oficios': lista_oficios}, context)

@login_required
def detalhes(request, numero):
    item = get_object_or_404(Oficio, numero=numero)
    if request.method == "POST":
        form = FormOficio(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'salvo.html', {})
    else:
        form = FormOficio(instance=item)
    context = RequestContext(request)
    return render(request, 'detalhes.html', {'form': form, 'item': item}, context)

@login_required
def novo(request):
    if request.method == "POST":
        form = FormOficio(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.responsavel = get_object_or_404(Responsavel, usuario=request.user)
            item.save()
            return render(request, 'salvo.html', {})
    else:
        form = FormOficio()
    context = RequestContext(request)
    return render(request, 'novo.html', {'form': form}, context)


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL  # Typically /static/
    sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL  # Typically /static/media/
    mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path

@login_required
def render_pdf_view(request, numero):
    template_path = 'user_printer.html'
    dados = get_object_or_404(Oficio, numero=numero, responsavel__usuario=request.user)
    converter = cnpj(dados.responsavel.setor.orgao.cnpj)
    context = {'dados': dados, 'converter': converter}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def visualizar(request, numero):
    item = get_object_or_404(Oficio, numero=numero, responsavel__usuario=request.user)
    converter = cnpj(item.responsavel.setor.orgao.cnpj)
    context = RequestContext(request)
    return render(request, 'visualizar.html', {'item': item, 'converter': converter}, context)

@login_required
def delete(request, numero):
    item = get_object_or_404(Oficio, numero=numero, responsavel__usuario=request.user)
    item.delete()
    context = RequestContext(request)
    return render(request, 'deletar.html', {'item': item}, context)


def do_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/oficio/')
    else:
        return redirect('/oficio/')
    return render(request,'login.html',{})

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login/')
    else:
        return redirect('/login/')


def home(request):
    return redirect('/login/')