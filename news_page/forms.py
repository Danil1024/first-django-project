from django import forms
from .models import *
from django.contrib.auth import authenticate


class RegistrationUser(forms.ModelForm):
	username = forms.CharField(label='Ник')

	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get('username')
		if username in MyUser.objects.values('username'):
			raise forms.ValidationError()

 
	class Meta:
		model = MyUser
		fields = ('first_name','last_name','username','password')


class AuthenticationForm(forms.Form):
	username = forms.CharField(label='Ник',required=True)
	password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput)
	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')
		self.user = authenticate(username=username, password=password)
		if self.user is None:
			raise forms.ValidationError('')
