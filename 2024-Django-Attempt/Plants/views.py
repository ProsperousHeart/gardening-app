from django.shortcuts import render, get_object_or_404
# from django.shortcuts import HttpResponse

import json
from django.core.paginator import Paginator
from django.core.serializers import serialize

from django.views.generic import ListView, DetailView#, TemplateView
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
    

    def get_paginated_context(self, queryset, page, limit):
        if not page:
            page = 1
        if limit:
            self.paginate_by = limit
        
        paginator = Paginator(queryset, self.page_limit)
        page_obj = paginator.get_page(page)
        serialized_page = serialize("json", page_obj.object_list)
        serialized_page = [obj['fields'] for obj in json.loads(serialized_page)]

        return {
            "data": serialized_page,
            "pagination": {
                "page": page,
                "limit": limit,
                "has_next": page_obj.has_next(),
                "has_prev": page_obj.has_previous(),
                "total": queryset.count()
            },
            'paginator': paginator,
            'page_obj': page_obj,
            'serialized_page': serialized_page
        }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_range'] = self.get_page_range(context['paginator'], context['page_obj'])
    #     return context

    # def get_page_range(self, paginator, current_page):
    #     current_index = current_page.number - 1
    #     start_index = max(0, current_index - 5)
    #     end_index = min(start_index + 10, paginator.num_pages)
    #     return range(start_index + 1, end_index + 1)

def PlantDetailView(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    context = {
        'plant': plant
    }
    return render(request, 'plants/plant_detail.html', context)

# class PlantDetailView(DetailView):
#     model = Plant
#     template_name = 'plants/plant_detail.html'
#     context_object_name = 'plant'

#     # def get_object(self, queryset=None):
#     #     # Retrieve the object based on a specific condition
#     #     # For example, retrieving based on a slug field
#     #     print(self.kwargs)
#     #     plant_id = self.kwargs.get('pk')
#     #     obj = get_object_or_404(Plant, pk=plant_id)
#     #     return obj
