from django.shortcuts import redirect, render

from zjvapp.forms import ThingForm
from zjvapp.models import Thing


def index(request):
    things = Thing.objects.all()
    return render(request, 'index.html', context={'things':things})


def thing_detail(request, slug):
    thing = Thing.objects.get(slug=slug)
    return render(request, 'thing_detail.html', context={'thing':thing})


def thing_edit(request, slug):
    thing = Thing.objects.get(slug=slug)
    if request.method == 'GET':
        form = ThingForm(instance=thing)
        # does thing really need to be in this template?
        return render(request, 'thing_edit.html', context={'thing':thing, 'form': form})
    if request.method == 'POST':
        form = ThingForm(data=request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_detail', slug=thing.slug)
