from django.shortcuts import render

from zjvapp.models import Thing


def index(request):
    things = Thing.objects.all()
    return render(request, 'index.html', context={'things':things})


def thing_detail(request, slug):
    thing = Thing.objects.get(slug=slug)
    return render(request, 'thing_detail.html', context={'thing':thing})
