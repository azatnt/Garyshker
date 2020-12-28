from .models import *
from django import forms





class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Написать', 'rows': 1, 'cols': 3}))
    class Meta:
        model = Comment
        fields = ('content',)




class ReportCreateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = (
            'genre',
            'title',
            'header',
            'body',
            'image'
        )

        widgets = {
            'body':forms.Textarea(attrs={'cols': 46, 'rows': 3}),
            'image': forms.FileInput()

        }
        # field_order = ['genre', 'title', 'body', 'header']

#
# class CommentEditForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = {
#             'content'
#         }
