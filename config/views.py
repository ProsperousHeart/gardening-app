# from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is gardening app temp page</h1>")