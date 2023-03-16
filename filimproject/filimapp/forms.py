from django import forms
from .models import Filim

class FilimForm(forms.ModelForm):
    class Meta:
        model=Filim
        fields=['name','desc','year','img']