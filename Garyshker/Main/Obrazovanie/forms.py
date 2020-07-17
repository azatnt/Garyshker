from .models import *
from django import forms





class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'comment', 'rows':'3', 'cols':'19'}))
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

#
# class CommentEditForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = {
#             'content'
#         }
