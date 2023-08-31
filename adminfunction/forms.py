from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs=
		{"autofocus": True,"class":"myuser"}))
password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class":"mypass"}),
    )

class PasswordChangingForm(PasswordChangeForm):
      old_password = forms.CharField(label=_("Old Password"),widget=forms.PasswordInput(attrs={'class':'form-control'}))
      new_password1 = forms.CharField(label=_("New Password"),widget=forms.PasswordInput(attrs={'class':'form-control'}))
      new_password2 = forms.CharField(label=_("Confirm Password"),widget=forms.PasswordInput(attrs={'class':'form-control'}))
      class Meta:
           model:User
           fields = ('old_password','new_password1','new_password2')