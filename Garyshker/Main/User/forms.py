from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput




class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Никнейм'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'Пароль'})
        self.fields['password'].label = False




class UserRegisterForm(UserCreationForm):
	# email = forms.EmailField()
	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': ("Пароль")})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': ("Подтвердите")})


	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
		widgets = {
		 'username':forms.TextInput(attrs = {'placeholder': 'Никнейм'}),
		 'email':forms.TextInput(attrs = {'placeholder': 'Email'}),
		 # 'password1' : forms.PasswordInput(attrs = {'placeholder': 'Password'}),
		 # 'password2':forms.TextInput(attrs = {'placeholder': 'Подтвердите'})
		}


		help_texts={
			'username': None
		}






class ProfileUpdateForm(forms.ModelForm):
	# images = forms.FileField(required=False, widget=forms.FileInput)


	class Meta:
		model = Profile
		fields = ['images',
				  'city',
				  'phone',
				  'age'
				  ]

		widgets = {
	             'images': forms.FileInput(),
	          }
		help_texts={
			'username': None
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
			'comments',
			# 'total_investment'
		]
