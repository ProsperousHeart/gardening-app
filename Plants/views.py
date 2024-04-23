from django.shortcuts import render
# from django.shortcuts import HttpResponse

from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Plant

# Create your views here.
# def plants(request):
#     # return HttpResponse("<h1>This is plant index temp page</h1>")
#     return render(request, 'plants/index.html', {})

class PlantListView(ListView):
    model = Plant
    template_name = 'plants/plant_list.html'
    context_object_name = 'plant_list'
    ordering = ['name_common']
    paginate_by = 10

class PlantDetailView(DetailView):
    model = Plant
    template_name = 'plants/plant_detail.html'
    context_object_name = 'plant'
