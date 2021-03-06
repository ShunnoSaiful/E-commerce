from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import Customer
User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Username'
		}))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'placeholder':'Password'
		}))


	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if not qs.exists():
			raise forms.ValidationError("Username is not valid")
		return username

	def clean_password(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		if user is None:
			raise forms.ValidationError("Password is not correct. Please enter valid one")
		return user



class RegisterForm(forms.ModelForm):
	first_name = forms.CharField(
		widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'First Name'
		}))
	last_name = forms.CharField(
		widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Last Name'
		}))
	username = forms.CharField(
		widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Username'
		}))
	email = forms.EmailField(
		widget=forms.EmailInput(
		attrs={
		'class':'form-control',
		'placeholder':'E-mail'
		}))
	password = forms.CharField(
		widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'placeholder':'Password'
		}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'placeholder':'Confirm Password'
		}))
	class Meta:
		model = Customer
		fields = [
			"first_name",
			"last_name",
			"username",
			"email",
			"password",
			"password2"
		]


	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username already taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("E-mail already taken")
		return email


	def clean_password2(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password2 != password:
			raise forms.ValidationError("Password doesn't match")
		return data


	