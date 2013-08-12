from django.contrib.auth import forms
from django.utils.translation import ugettext, ugettext_lazy as _

class LoginForm(forms.AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder':'login'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'placeholder':'login'}))