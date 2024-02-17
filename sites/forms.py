from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#translating the form in french
from django.utils.translation import gettext_lazy as _

from .models import Site


class SiteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Site
        fields = '__all__'


class UserRegistrationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("Les deux mots de passe ne correspondent pas."),
        'username_exists': _("Ce nom d'utilisateur existe déjà."),
    }
    username = forms.CharField(label=_("Nom d'utilisateur"))
    password1 = forms.CharField(label=_("Mot de passe"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Confirmation du mot de passe"), widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
