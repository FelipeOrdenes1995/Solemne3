from django import forms
from django.forms import ModelForm
from django.forms import fields
from .models import Plan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PlanForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=200)
    precio = forms.IntegerField(min_value=0, max_value=999999)
    class Meta:
        model= Plan
        fields = ['nombre','precio','servicio','contenido']

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'username','password1','password2']
    