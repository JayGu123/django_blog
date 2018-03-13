from django import forms
from .models import POST

class postForm(forms.ModelForm):
    class Meta:
        model = POST
        fields = ('title', 'text',)
