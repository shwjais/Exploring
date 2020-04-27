from django.contrib.auth.models import User
from level_five_app.models import userinfo
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields = ('username', 'email', 'password')

class userinfoform(forms.ModelForm):
    class Meta():
        model = userinfo
        fields = ('portfolio_site', 'profile_image')

