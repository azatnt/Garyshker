from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *





class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()


	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
		help_texts={
			'username': None
		}



class ProfileUpdateForm(forms.ModelForm):
	image = forms.ImageField(required=False, widget=forms.FileInput)


	class Meta:
		model = Profile
		fields = ['image',
				  'city',
				  'phone',
				  'age'
				  ]
		help_texts={
			'username': None,
			'image': None
		}



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()


	class Meta:
		model = User
		fields = ['username',
				  'first_name',
				  'last_name',
				  'email'
				  ]
		help_texts={
			'username': None
		}




class CharityAuthorForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = [
			'city',
			'phone',
			'investment',
			'comments',
			# 'total_investment'
		]
