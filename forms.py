from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.models import ModelForm 
from .models import Booking, Room


class RegisterForm(UserCreationForm):
    First_Name = forms.CharField(max_length=30)
    Last_Name = forms.CharField(max_length=30)
    CNIC = forms.IntegerField()
    Contact_Number = forms.IntegerField()
    Email = forms.EmailField(max_length=254)

    
    class Meta:
        model = User
        fields = ("username", "First_Name", "Last_Name", "CNIC", "Contact_Number", "Email", "password1","password2",)


class Add_room(ModelForm):
    class Meta:
        model = Room
        fields ='__all__'

class Book_Room_User(ModelForm):
    class Meta:
        model = Booking
        fields ='__all__'