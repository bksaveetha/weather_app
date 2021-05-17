from django.forms import ModelForm ,TextInput
from .models import CITY

class CityForm(ModelForm):
    class Meta:
        model = CITY
        fields  = ['name']
        widejets = {'name' : TextInput(attrs={'class' : 'input' , 'placeholder' : 'City Name'})}