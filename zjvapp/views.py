from django.shortcuts import render

from zjvapp.models import Thing

def index(request):
    return render(request, 'index.html')
