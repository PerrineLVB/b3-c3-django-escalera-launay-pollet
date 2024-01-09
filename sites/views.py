from django.shortcuts import render
from django.http import HttpResponse
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
        try:
            name = request.POST.get('name')
            username = request.POST.get('username')
            site_url = request.POST.get('site_url')
            password = request.POST.get('password')
            site = Site(name=name, username=username, site_url=site_url, password=password)
            site.save()
            return HttpResponse('Site created successfully')
        except(Exception):
            #todo: see which exception
            return HttpResponse('error 500')
    return render(request, 'create_site.html')

def update_site(request, pk):
    site = Site.objects.filter(pk=pk).first()
    if site is not None:
        if request.method == 'POST':
            name = request.POST.get('name')
            username = request.POST.get('username')
            site_url = request.POST.get('site_url')
            password = request.POST.get('password')
            site.name = name
            site.username = username
            site.site_url = site_url
            site.password = password
            site.save()
            return HttpResponse('Site updated successfully')
        context = {'site': site}
        return render(request, 'update_site.html', context)
    #todo: find errorType
    return HttpResponse('bad request')

def delete_site(request, pk):
    site = Site.objects.filter(pk=pk).first()
    if site is not None:
        site.delete()
        return HttpResponse('Site deleted successfully')
    return HttpResponse('bad request')