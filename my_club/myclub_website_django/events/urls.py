from django.urls import path
from .import views

urlpatterns = [
	#int: 
	#str:
	#path: Urls/
	#slug: hyphen-and_underscores
	#UUID: uuid
	path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.events, name="events"),
    path('add_venue', views.add_venue, name="add_venue"),
    path('venues', views.venues, name="venues"),
    path('show_venues/<venue_id>', views.show_venue, name='show_venue'),
    path('search_venues', views.search_venues, name='search_venues'),
    path('update_venue/<venue_id>', views.update_venue, name='update_venue'),
    path('add_event', views.add_event, name='add_event'),
    path('update_event<event_id>', views.update_event, name='update_event'),
    path('show_event/<event_id>', views.show_event, name='show_event'),


]
   
