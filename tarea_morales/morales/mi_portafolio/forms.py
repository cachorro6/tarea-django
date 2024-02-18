from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','address','phone','age','pelicula_favorita','ultima_pelicula_vista')
