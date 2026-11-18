from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
]
