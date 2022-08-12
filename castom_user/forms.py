from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationUser(UserCreationForm):
	password1 = forms.CharField(label='пароль',required=True, widget=forms.PasswordInput)
	password2 = forms.CharField(label='повторите пароль',required=True, widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('first_name','last_name','username')