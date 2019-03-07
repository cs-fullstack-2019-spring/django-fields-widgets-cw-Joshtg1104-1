from django.shortcuts import render
from django.http import HttpResponse
from .forms import SuperHeroForm


# Create your views here.

def index(request):
    return render(request, "FieldsWidgetsCWApp/index.html")

def heroApp(request):
    if request.method == "POST":
        return render(request, "FieldsWidgetsCWApp/congrats.html")
    return render(request, "FieldsWidgetsCWApp/heroApp.html", {"heroform": SuperHeroForm})

