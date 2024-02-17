import csv, io

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from sites.forms import SiteForm, UserRegistrationForm
# Create your views here.
from sites.models import Site
from django.contrib import messages

from sites.utils import detect_delimiter


@login_required(redirect_field_name=None)
def index(request):
    sites = Site.objects.all()
    context = {'sites': sites}
    # clean messages in session
    storage = messages.get_messages(request)

    for message in storage:
        pass

    # Marquer les messages comme utilisés
    storage.used = True
    return render(request, 'index.html', context)


@login_required(redirect_field_name=None)
def site_details(request, pk):
    site = Site.objects.filter(pk=pk).first()
    context = {'site': site}
    return render(request, 'site_details.html', context)


@login_required(redirect_field_name=None)
def create_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre site a été ajouté avec succès !')
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


@login_required(redirect_field_name=None)
def update_site(request, pk):
    site = Site.objects.filter(pk=pk).first()

    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre site a été ajouté avec succès !')
        else:
            messages.error(request, 'Un problème est survenu lors de l\'ajout de votre site')
        return redirect('/sites')

    else:
        form = SiteForm(instance=site)
        # return HttpResponse('Votre site a été modifié avec succès')

    return render(request,
                  'update_site.html',
                  {'form': form})


@login_required(redirect_field_name=None)
def delete_site(request, pk):
    site = Site.objects.get(pk=pk)
    if request.method == 'POST':
        site.delete()
        messages.success(request, 'Votre site "' + site.name + '" a été supprimé avec succès.')
        return redirect('/sites')

    return render(request, 'delete_site.html',{'site': site})


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sites.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'username', 'site_url', 'password'])
    sites = Site.objects.all()
    for site in sites:
        writer.writerow([site.name, site.username, site.site_url, site.password])

    return response


def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        next(io_string)
        detected_delimiter = detect_delimiter(decoded_file)
        for row in csv.reader(io_string, delimiter=detected_delimiter, quotechar='|'):
            _, created = Site.objects.update_or_create(
                name=row[0],
                username=row[1],
                site_url=row[2],
                password=row[3]
            )
        return redirect('/sites')
    return render(request, 'import_csv.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Rediriger vers la page de connexion après l'inscription réussie
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
