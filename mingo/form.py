from django import forms

_FINS = [('falcate', 'Falcate'), ('triangular', 'Triangular'), ('rounded', 'Rounded')]
_WHALES = [('humpback', 'Humpback'), ('orca', 'Orca'), ('blue', 'Blue'),
           ('killer', 'Killer'), ('begula', 'Begula'), ('fin', 'Fin'), ('gray', 'Gray'),
           ('sperm', 'Sperm')]
_BLOWS = [('tall', 'Tall'), ('bushy', 'Bushy'), ('dense', 'Dense')]
_WAVES = [('flat', 'Flat'), ('small', 'Small'), ('moderate', 'Moderate'), ('large', 'Large'),
          ('breaking', 'Breaking'), ('high', 'High')]

class Sighting(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    data = forms.CharField()
    time = forms.CharField()
    location = forms.CharField()
    fin_type = forms.ChoiceField(choices=_FINS)
    whale_type = forms.ChoiceField(choices=_WHALES)
    blow_type = forms.ChoiceField(choices=_BLOWS)
    wave_type = forms.ChoiceField(choices=_WAVES)

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
