from django.shortcuts import render, redirect
from django.http import HttpResponse

from sites.forms import SiteForm
# Create your views here.
from sites.models import Site
from django.contrib import messages


def index(request):
    from datetime import datetime, timedelta

    # Récupérer la date du 1er juin de cette année
    premier_juin = datetime.now().replace(month=6, day=1)

    # Calculer le nombre de jours à ajouter pour atteindre le premier lundi
    jours_avant_lundi = (7 - premier_juin.weekday()) % 7

    # Ajouter les jours nécessaires pour atteindre le premier lundi
    premier_lundi_juin = premier_juin + timedelta(days=jours_avant_lundi)

    # Afficher le résultat
    print(f"Le premier lundi du mois de juin est le {premier_lundi_juin.strftime('%Y-%m-%d')}.")
    sites = Site.objects.all()
    context = {'sites': sites}
    #clean messages in session
    storage = messages.get_messages(request)

    for message in storage:
       pass

    # Marquer les messages comme utilisés
    storage.used = True
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
            messages.success(request, 'Votre site a été ajouté avec succès')
        else:
            messages.error(request, 'Un problème est survenu lors de l\'ajout de votre site')
        return redirect('/sites')
            # return HttpResponse('Votre site a été ajouté avec succès')
    # if request.method == 'GET', form is empty
    else:
        form = SiteForm()

    return render(request,
                  'create_site.html',
                  {'form': form})


def update_site(request, pk):
    site = Site.objects.filter(pk=pk).first()

    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre site a été ajouté avec succès')
        else:
            messages.error(request, 'Un problème est survenu lors de l\'ajout de votre site')
        return redirect('/sites')

    else:
        form = SiteForm(instance=site)
            # return HttpResponse('Votre site a été modifié avec succès')

    return render(request,
                  'update_site.html',
                  {'form': form})


def delete_site(request, pk):
    site = Site.objects.filter(pk=pk).first()
    if site is not None:
        site.delete()
        return HttpResponse('Site deleted successfully')
    return HttpResponse('bad request')
