from django.shortcuts import render, redirect
from django.http import HttpResponse

from sites.forms import SiteForm
# Create your views here.
from sites.models import Site


def index(request):
    sites = Site.objects.all()
    context = {'sites': sites}
    return render(request, 'index.html', context)


def site_details(request, pk):
    site = Site.objects.filter(pk=pk).first()
    context = {'site': site}
    return render(request, 'site_details.html', context)


def create_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sites')
            # return HttpResponse('Votre site a été ajouté avec succès')
    # if request.method == 'GET', form is empty
    else:
        form = SiteForm()

    return render(request,
                  'create_site.html',
                  {'form': form})


def update_site(request, pk):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sites')
        # return HttpResponse('Votre site a été ajouté avec succès')
    # if request.method == 'GET', form is empty
    else:
        site = Site.objects.get(id=pk)
        form = SiteForm()

    return render(request,
                  'update_site.html',
                  {'form': form})


def delete_site(request, pk):
    site = Site.objects.filter(pk=pk).first()
    if site is not None:
        site.delete()
        return HttpResponse('Site deleted successfully')
    return HttpResponse('bad request')
