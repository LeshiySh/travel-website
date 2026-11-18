from django.shortcuts import render, get_object_or_404
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

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tour_detail.html', {'tour': tour})