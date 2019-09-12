from django.forms import ModelForm

from zjvapp.models import Thing

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description')