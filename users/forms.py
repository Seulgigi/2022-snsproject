from unicodedata import name
from allauth.account.forms import SignupForm
from django import forms
from cProfile import label
from .models import *

class MyCustomSignupForm(SignupForm):
    name = forms.CharField(
        max_length=10,
        label="name",
        widget=forms.TextInput(),
    )

    password1 = forms.CharField(
        min_length=8,
        label="password",
        widget=forms.PasswordInput(),
        
        )

    password2 = forms.CharField(
        widget=forms.PasswordInput(), 
        label="Confirm Password",
        )

    email = forms.CharField(
        max_length=40,
        label="email",
        widget=forms.TextInput(
            attrs = {
                "type":"email",
                "placeholder":"a@a.com",
            }
        ),
    )

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.save()
        profile = Profile()
        profile.user = user
        profile.name = self.cleaned_data.get('name')
        profile.email = self.cleaned_data.get('email')
        profile.save()
        return user