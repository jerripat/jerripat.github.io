from django import forms
from.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'email_name', 'text']
        labels = {
            'user_name': 'Your Name',
            'email_name': 'Your Email',
            'text': 'Your Comment',
        }