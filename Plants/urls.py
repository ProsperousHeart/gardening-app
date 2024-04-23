from django.urls import path

from Plants.views import PlantListView, PlantDetailView  #, plants

urlpatterns = [
    # path('', plants),
    # path('plants-list/', PlantListView.as_view(), name='plants-list')
    path('', PlantListView.as_view(), name='plants'),
    path('<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
]
