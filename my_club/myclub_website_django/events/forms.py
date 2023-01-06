from django import forms
from django.forms import ModelForm
from .models import Venue, Event



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


class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'event_date', 'venue', 'manager', 'description',]
		labels = {'name': '', 'event_date': 'YYYY-MM-DD HH:MM:SS','venue': 'Venue', 'manager':'Manager', 'description':'',}
		widgets={'name': forms.TextInput(attrs={'class': 'form', 'placeholder':'Event name'}),
		'event_date': forms.TextInput(attrs={'class': 'form-controll', 'placeholder':'Date '}),
		'venue': forms.Select(attrs={'class': 'select', 'placeholder':'Venue name'}), 
		'manager': forms.Select(attrs={'class': 'elect', 'placeholder':'Manager'}),
		'description': forms.Textarea(attrs={'class': 'form-controll', 'placeholder':'Description'})}