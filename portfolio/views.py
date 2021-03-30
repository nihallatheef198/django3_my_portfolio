from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    contents = models.project.objects.all()
    return render(request,'portfolio/home.html',{'contents': contents})
