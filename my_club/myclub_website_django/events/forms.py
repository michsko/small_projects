from django import forms
from django.forms import ModelForm
from .models import Venue



#create form for Venue 

class VenueForm(ModulForm):
	class Meta:
		model = Venue
		fields = ('name', 'address', 'phone', 'emil_address',)    #  "__all__"
