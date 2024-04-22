from django.shortcuts import render
# from django.shortcuts import HttpResponse

# Create your views here.
def plants(request):
    # return HttpResponse("<h1>This is plant index temp page</h1>")
    return render(request, 'plants/index.html', {})