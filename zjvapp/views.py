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
    form_class = ThingForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():  # necessary? paradigm? why not try/catch?
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    else:
        form = form_class(instance=thing)

    return render(request, 'thing_edit.html', context={'thing':thing, 'form': form})
