from django import forms

_FINS = ['Falcate', 'Triangular', 'Rounded']
_WHALES = ['Humpback', 'Orca', 'Blue', 'Killer', 'Begula', 'Fin', 'Gray', 'Sperm']
_BLOWS = ['Tall', 'Bushy', 'Dense']
_WAVES = ['Flat', 'Small', 'Moderate', 'Large', 'Breaking', 'High']

class Sighting(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    data = forms.CharField()
    time = forms.CharField()
    location = forms.CharField()
    fin_type = forms.CharField()
    whale_type = forms.CharField()
    blow_type = forms.CharField()
    wave_type = forms.CharField()