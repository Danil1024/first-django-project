from django import forms
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationUser(UserCreationForm):
	password1 = forms.CharField(label='пароль',required=True, widget=forms.PasswordInput)
	password2 = forms.CharField(label='повторите пароль',required=True, widget=forms.PasswordInput)
	class Meta:
		model = MyUser
		fields = ('first_name','last_name','username')