from django.shortcuts import render

# Create your views here.
def flask(request):
    return render(request,"flask.html")

def pyramid(request):
    return render(request,"pyramid.html")

def django(request):
    return render(request,"django.html")