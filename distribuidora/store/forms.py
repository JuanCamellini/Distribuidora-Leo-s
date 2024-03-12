from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='')
    email = forms.EmailField(label='')
    phone = forms.CharField(max_length=50)
    empresa = forms.CharField(max_length=63)
    password1 = forms.CharField(label='', widget=forms.PasswordInput)
    password2 = forms.CharField(label='', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'email','style':'width:600px;display:block','type':'text' ,'placeholder':"enter your username"})
        self.fields['password1'].widget.attrs.update({'class':'email', 'style':'width:600px', 'placeholder':"enter your password"})
        self.fields['password2'].widget.attrs.update({'class':'email', 'style':'width:600px' , 'placeholder':"repeat your password"})
        self.fields['email'].widget.attrs.update({'class':'email', 'style':'width:600px' ,'type':'email','placeholder':"enter your email"})
        fields = ['username', 'email', 'password1', 'password2']
        for fieldname in fields:
            self.fields[fieldname].help_text = None