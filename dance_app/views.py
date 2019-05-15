from django.shortcuts import render, HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("url and views index function works") # sanity check

def index(request):
    return render(request, "index.html")
