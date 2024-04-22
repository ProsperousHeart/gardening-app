from django.urls import path

from Plants.views import plants

urlpatterns = [
    path('', plants),
]
