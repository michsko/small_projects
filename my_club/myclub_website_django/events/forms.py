from django import forms
from django.forms import ModelForm
from .models import Venue



#create form for Venue 

class VenueForm(forms.ModelForm):
	class Meta:
		model = Venue
		fields = ['name', 'address', 'phone', 'email_address',]   #  "__all__"
		labels = {'name': '' , 'address': '', 'phone': '', 'email_address': '',}
		widgets = {'name': forms.TextInput(attrs={'class': 'form-controll', 'placeholder':'Venue name'}),
		'address': forms.TextInput(attrs={'class': 'form-controll', 'placeholder':'Venue address'}),
		'phone':forms.TextInput(attrs={'class': 'form-controll','placeholder':'Venue phone'}),
		'email_address' :forms.EmailInput(attrs={'class': 'form-controll','placeholder':'Venue email_address'})}