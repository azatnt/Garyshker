from .models import *
from django import forms





class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here!', 'rows':'4', 'cols':'20'}))
    class Meta:
        model = Comment
        fields = ('content',)



class ReportCreateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = {
            'title',
            'genre',
            'body'
        }
