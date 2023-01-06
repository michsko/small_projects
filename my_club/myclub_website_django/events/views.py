from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm 

# Create your views here.


def add_venue(request):
	submitted = False
	if request.method == "POST":
		form = VenueForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/add_venue?submitted=True")
	else: 
		form = VenueForm
		if "submitted" in request.GET:
			submitted = True

	return render(request, 'events/add_venue.html',{
		'form': form,
		'submitted': submitted
		})



def add_event(request):
	submitted = False
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/add_event?submitted=True")
	else: 
		form = EventForm
		if "submitted" in request.GET:
			submitted = True

	return render(request, 'events/add_event.html',{
		'form': form,
		'submitted': submitted
		})




def events(request):
	events = Event.objects.all()

	return render(request, 'events/events.html', {
		"events": events, 
		})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	name = "John"
	#Convert month from name to number
	month = month.capitalize()
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# crate a claendar
	cal = HTMLCalendar().formatmonth(
		year,
		month_number)

	# get current year
	now = datetime.now()
	current_year = now.year

	# get current time 
	time = now.strftime('%H:%M:%S')

	return render(request,
		'events/home.html', {
		"name" : name, 
		"year": year,
		"month": month,
		"month_number": month_number,
		"cal": cal,
		"current_year": current_year,
		"time": time, 	
		})


def venues(request):
	venue_list = Venue.objects.all()

	return render(request, 'events/venues.html',{
		'venue_list': venue_list,
		})


def search_venues(request):
	if request.method == 'POST':
		searched = request.POST['searched']
		venues = Venue.objects.filter(name__contains=searched)
		
		return render(request, "events/search_venues.html",{
			'searched': searched,
			'venues': venues,
			})

	else:
		return render(request, "events/search_venues.html",{})


def show_event(request, event_id):
	event = Event.objects.get(pk=event_id)

	return render(request, "events/show_event.html",{
		'event': event
		})


def show_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)

	return render(request,"events/show_venue.html",{
		'venue': venue, 
		})


def update_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('events')

	return render(request,"events/update_event.html",{
		'event': event,
		'form': form,
		})


def update_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	form = VenueForm(request.POST or None, instance=venue)
	if form.is_valid():
		form.save()
		return redirect('venues')

	return render(request,"events/update_venue.html",{
		'venue': venue,
		'form': form,
		})
