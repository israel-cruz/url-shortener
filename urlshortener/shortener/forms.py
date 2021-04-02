from django import forms
from .models import Url

class UrlForm(forms.ModelForm):
    link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Paste your long url here'}))

    class Meta:
        model = Url
        fields = '__all__'