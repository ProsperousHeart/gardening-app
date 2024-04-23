from django.urls import path

from Plants.views import PlantListView, PlantDetailView #, HomeView  #, plants

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    # path('plants-list/', PlantListView.as_view(), name='plants-list')
    path('', PlantListView.as_view(), name='plants'),
    # path('list/', PlantListView.as_view(), name='plants'),
    path('<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
]
