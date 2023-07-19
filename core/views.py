from django.shortcuts import render
from . models import Website

# Create your views here.
def home_view(request):
    name = "Welcome to "

    obj = Website.objects.get(id=3)

    context = {
        'name': name,
        'obj' : obj,
    }

    return render(request, 'core/index.html', context)