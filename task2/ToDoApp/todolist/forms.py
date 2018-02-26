from django import forms
from django.contrib.auth.forms import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


class NewTaskForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())

