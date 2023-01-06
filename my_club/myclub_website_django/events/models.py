from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=120)
	address = models.CharField(max_length=120, blank=True)
	zip_code = models.CharField('Zip_code', max_length=120, blank=True)
	phone = models.CharField('Contact Phone', max_length=120, blank=True)
	web = models.URLField('Website Address', blank=True)
	email_address = models.EmailField('Email Address', blank=True)

	def __str__(self):
		return self.name



class Member (models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	member_email = models.EmailField('Member Email')


	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_length=120)
	#manager = models.CharField(max_length=60, blank=True)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(Member, blank=True)
	
	def __str__(self):
		return self.name


