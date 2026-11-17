from django.shortcuts import render
from .models import Tour

def index(request):
    return render(request, 'index.html')

def catalog(request):
    query = request.GET.get('q', '')
    if query:
        tours = Tour.objects.filter(title__icontains=query)
    else:
        tours = Tour.objects.all()
    return render(request, 'catalog.html', {'tours': tours, 'query': query})
