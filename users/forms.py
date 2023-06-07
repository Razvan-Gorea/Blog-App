from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create a form that inherits from UserCreationForm

class UserRegisterForm(UserCreationForm): # UserRegisterForm inherits from UserCreationForm
    email = forms.EmailField() # default is required=True

    class Meta:
        model = User # model that will be affected
        fields = ['username', 'email', 'password1', 'password2'] # fields that will be displayed on the form and in what order