from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import SBUser

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = SBUser
        fields = ('username', 'email', 'password1', 'password2', 'planet')