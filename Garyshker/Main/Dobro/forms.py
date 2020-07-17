from .models import *
from django import forms





class InvestForm(forms.ModelForm):
	class Meta:
		model = Dobro
		fields = [
			'investment',
			'comments'
		]
