from django.shortcuts import render

from zjvapp.models import Thing

def index(request):
    things = Thing.objects.all()
    return render(request, 'index.html', context={'things':things})
