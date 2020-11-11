from django import forms

from .models import Article
from django.contrib.auth.forms import AuthenticationForm

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =[
            'title',
            'content',
            'active',
        ]
    

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_validated:
            raise forms.ValidationError('There was a problem with your login.', code='invalid_login')        