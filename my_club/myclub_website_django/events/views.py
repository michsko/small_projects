from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm 
from django.http import HttpResponse
import csv
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



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



def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	event.delete()
	
	return redirect('events')

def delete_venue(request, venue_id):
	venue = Venue.objects.get(pk=venue_id)
	venue.delete()

	return redirect('venues')


def events(request):
	events = Event.objects.all().order_by('event_date')

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
	venue_list = Venue.objects.all().order_by('name')

	return render(request, 'events/venues.html',{
		'venue_list': venue_list,
		})

def venue_text(request):
	response = HttpResponse(content_type='text/plain')
	
	response['Content=Disposition']= 'attachment; filename=venues.txt'

	venues = Venue.objects.all()

	lines = []
	
	for venue in venues:

		lines.append(f'{venue.name}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n')

	response.writelines(lines)
	return response



def venue_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Conternt=Disposition'] = 'attachment; filename=venue.csv'

	writer = csv.writer(response)
	venues = Venue.objects.all()

	writer.writerow(['Venue Name', 'Venue Address', 'Phone', 'Web', 'email_address'])
	
	for venue in venues: 
		writer.writerow([venue.name, venue.address, venue.phone, venue.web,  venue.email_address])

	return response


def venue_pdf(request):
	#create bytestresm buffer

	buff = io.BytesIO()

	# create a canvas 
	canv = canvas.Canvas(buff, pagesize=letter, bottomup=0)

	# create a textobject 
	textob = canv.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont('Helvetica', 14)


	# add lines 
	lines = ['this is line1',
	'this is line 2']

	# loop through 

	for line in lines: 
		textob.textLine(line)

	canv.drawText(textob)
	canv.showPage()
	canv.save()
	buff.seek(0)

	return FileResponse(buff, as_attachment=True, filename='venue.pdf')




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
