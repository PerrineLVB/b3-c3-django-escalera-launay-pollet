from django import forms
from .models import Site


class SiteForm(forms.ModelForm):
    site_url = forms.URLField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Site
        fields = '__all__'
