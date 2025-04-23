from django import forms
from posts.models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = [
            'post'
        ]
        widgets = {
            'comment':forms.Textarea(attrs={'class':'form-control'})
        }