from django.shortcuts import render, get_object_or_404
# from django.shortcuts import HttpResponse

from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Plant

# Create your views here.
# class HomeView(TemplateView):
#     template_name = 'Plants/index.html'

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

    # def get_object(self, queryset=None):
    #     # Retrieve the object based on a specific condition
    #     # For example, retrieving based on a slug field
    #     print(self.kwargs)
    #     plant_id = self.kwargs.get('pk')
    #     obj = get_object_or_404(Plant, pk=plant_id)
    #     return obj
